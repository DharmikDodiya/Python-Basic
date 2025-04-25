import os,json,random,mysql.connector
from cryptography.fernet import Fernet
from getpass import getpass
from mysql.connector import Error
from tabulate import tabulate

CONFIG_FILE = "creds/db_config.json"
SECRET_KEY_FILE = "creds/secret.key"

class BankAccountManager:
    def __init__(self):
        self.secret_key = self.load_or_create_secret_key()
        self.db_config = self.get_or_create_db_config()
        self.db_config, self.DB_NAME, self.TABLE_NAME = self.get_valid_db_config()
        self.conn = self.create_connection()


    def load_or_create_secret_key(self):
        os.makedirs("creds", exist_ok=True)
        if os.path.exists(SECRET_KEY_FILE):
            with open(SECRET_KEY_FILE, 'rb') as f:
                return f.read()
        key = Fernet.generate_key()
        with open(SECRET_KEY_FILE, 'wb') as f:
            f.write(key)
        return key

    def encrypt_pin(self, pin):
        fernet = Fernet(self.secret_key)
        return fernet.encrypt(pin.encode()).decode()

    def decrypt_pin(self, encrypted_pin):
        fernet = Fernet(self.secret_key)
        return fernet.decrypt(encrypted_pin.encode()).decode()

   
    def get_or_create_db_config(self):
        key = self.load_or_create_secret_key()
        fernet = Fernet(key)

        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'rb') as f:
                encrypted_data = f.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            return json.loads(decrypted_data.decode())

        print("==== Enter MySQL Credentials ====")

        def required_input(text, is_password=False):        
            while True:
                value = getpass(text) if is_password else input(text).strip()
                if value:
                    return value
                print(f"{text.strip(': ')} is required.")

        host = input("Host (default: localhost): ").strip() or "localhost"
        user = required_input("MySQL Username (e.g., root): ")
        password = required_input("MySQL Password: ", is_password=True)
        db_name = input("Enter Database Name (e.g., bank_simulator): ") or "bank_simulator"
        table_name = input("Enter Table Name (e.g., accounts): ") or "accounts"

        config = {"host": host, "user": user, "password": password, "db_name": db_name, "table_name": table_name}
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        encrypted_config = fernet.encrypt(json.dumps(config).encode())
        with open(CONFIG_FILE, 'wb') as f:
            f.write(encrypted_config)

        return config

    def create_connection(self):
        return mysql.connector.connect(
            host=self.db_config["host"],
            user=self.db_config["user"],
            password=self.db_config["password"],
            database=self.DB_NAME
        )

    def setup_account_db_table(self):
        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(
                host=self.db_config["host"],
                user=self.db_config["user"],
                password=self.db_config["password"]
            )
            db_name = self.db_config["db_name"]
            table_name = self.db_config["table_name"]

            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            cursor.execute(f"USE {db_name}")
            cursor.execute(f"""
                CREATE TABLE IF NOT EXISTS {table_name} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    account_holder_name VARCHAR(255) NOT NULL,
                    account_number VARCHAR(12) UNIQUE NOT NULL,
                    amount FLOAT DEFAULT 0,
                    pin TEXT NOT NULL
                )
            """)
            return True, db_name, table_name
        except Error as e:
            print("Database setup error:", e)
            return False, None, None
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def get_valid_db_config(self):
        attempt = 0
        while True:
            config = self.get_or_create_db_config()
            success, db_name, table_name = self.setup_account_db_table()
            if success:
                return config, db_name, table_name
            else:
                attempt += 1
                if os.path.exists(CONFIG_FILE):
                    os.remove(CONFIG_FILE)
                print(f"\nAttempt {attempt}: Invalid credentials. Please try again...\n")

    def create_account(self, name, pin, amount):
        account_number = str(random.randint(100000000000, 999999999999))
        encrypted_pin = self.encrypt_pin(pin)
        cursor = self.conn.cursor()
        cursor.execute(f"""
            INSERT INTO {self.TABLE_NAME} (account_holder_name, account_number, amount, pin)
            VALUES (%s, %s, %s, %s)
        """, (name, account_number, amount, encrypted_pin))
        self.conn.commit()
        cursor.close()
        print(f"Account created successfully! Account Number: {account_number}")

    def get_account(self, account_number):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {self.TABLE_NAME} WHERE account_number = %s", (account_number,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def validate_pin(self, stored_pin, input_pin):
        try:
            return self.decrypt_pin(stored_pin) == input_pin
        except Exception:
            return False

    def show_account(self, account_number, pin):
        account = self.get_account(account_number)
        if account and self.validate_pin(account["pin"], pin):
            display_data = [{
                "Account Number": account["account_number"],
                "Name": account["account_holder_name"],
                "Balance": account["amount"]
            }]
            print("\n------------ Account Details ------------")
            print(tabulate(display_data, headers="keys", tablefmt="grid"))
        else:
            print("Invalid account or PIN.")

    def deposit(self, account_number, amount, pin):
        account = self.get_account(account_number)
        if account and self.validate_pin(account["pin"], pin):
            new_amount = account["amount"] + amount
            cursor = self.conn.cursor()
            cursor.execute(f"""
                UPDATE {self.TABLE_NAME} SET amount = %s WHERE account_number = %s
            """, (new_amount, account_number))
            self.conn.commit()
            cursor.close()
            print(f"Deposited successfully! New Balance: {new_amount}")
        else:
            print("Invalid account or PIN.")

    def withdraw(self, account_number, amount, pin):
        account = self.get_account(account_number)
        if account and self.validate_pin(account["pin"], pin):
            if account["amount"] >= amount:
                new_amount = account["amount"] - amount
                cursor = self.conn.cursor()
                cursor.execute(f"""
                    UPDATE {self.TABLE_NAME} SET amount = %s WHERE account_number = %s
                """, (new_amount, account_number))
                self.conn.commit()
                cursor.close()
                print(f"Withdrawn successfully! New Balance: {new_amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid account or PIN.")

    def delete_account(self, account_number, pin):
        account = self.get_account(account_number)
        if account and self.validate_pin(account["pin"], pin):
            cursor = self.conn.cursor()
            cursor.execute(f"DELETE FROM {self.TABLE_NAME} WHERE account_number = %s", (account_number,))
            self.conn.commit()
            cursor.close()
            print("Account deleted successfully.")
        else:
            print("Invalid account or PIN.")
