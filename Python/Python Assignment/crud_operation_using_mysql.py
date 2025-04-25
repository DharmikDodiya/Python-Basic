import mysql.connector
import os
import json
from mysql.connector import Error
from tabulate import tabulate
from cryptography.fernet import Fernet
from getpass import getpass


SECRET_KEY_FILE = "creds/secret.key"
CONFIG_FILE = "creds/db_config.json"

def load_or_create_secret_key():
    if os.path.exists(SECRET_KEY_FILE):
        with open(SECRET_KEY_FILE, 'rb') as f:
            return f.read()
    key = Fernet.generate_key()
    with open(SECRET_KEY_FILE, 'wb') as f:
        f.write(key)
    return key


def get_or_create_db_config():
    key = load_or_create_secret_key()
    fernet = Fernet(key)

    # if os.path.exists(CONFIG_FILE):
    #     with open(CONFIG_FILE, 'r') as f:
    #         return json.load(f)

    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())

    print("==== Enter MySQL Credentials ====")

    def required_input(prompt_text, is_password=False):
        while True:
            value = getpass(prompt_text) if is_password else input(prompt_text).strip()
            if value:
                return value
            print(f"{prompt_text.strip(': ')} is required.")

    host = input("Host (default: localhost): ").strip() or "localhost"
    user = required_input("MySQL Username (e.g., root): ")
    password = required_input("MySQL Password: ", is_password=True)

    # config = {"host": host, "user": user, "password": password}
    # with open(CONFIG_FILE, 'w') as f:
    #     json.dump(config, f)

    config = {"host": host, "user": user, "password": password}
    encrypted_config = fernet.encrypt(json.dumps(config).encode())
    
    with open(CONFIG_FILE, 'wb') as f:
        f.write(encrypted_config)

    return config

def setup_database_and_table(config):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"]
        )
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS user_db")
        cursor.execute("USE user_db")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                age INT
            )
        """)
        return True
    except Error as e:
        print("Database setup error:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Updated credential fetch with retry
def get_valid_db_config():
    attempt = 0
    while True:
        config = get_or_create_db_config()
        if setup_database_and_table(config):
            return config
        else:
            attempt += 1
            if os.path.exists(CONFIG_FILE):
                os.remove(CONFIG_FILE)
            print(f"\nAttempt {attempt}: Invalid credentials. Please try again...\n")

def connect_db():
    return mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database="user_db"
    )

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    age = input("Enter age: ")

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
        conn.commit()
        print("User created successfully!")
    except Error as err:
        print("Error:", err)
    finally:
        cursor.close()
        conn.close()

def read_users():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("\n--- User List ---")
    if rows:
        print(tabulate(rows, headers=["ID", "Name", "Email", "Age"], tablefmt="grid"))
    else:
        print("No users found.")
    cursor.close()
    conn.close()

def update_user():
    user_id = input("Enter user ID to update: ")
    name = input("Enter new name: ")
    email = input("Enter new email: ")
    age = input("Enter new age: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s, email=%s, age=%s WHERE id=%s", (name, email, age, user_id))
    conn.commit()
    print("User updated successfully!")
    cursor.close()
    conn.close()

def delete_user():
    user_id = input("Enter user ID to delete: ")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    print("User deleted successfully!")
    cursor.close()
    conn.close()

def menu():
    while True:
        print("\n===== User Management System =====")
        print("1. Create User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            read_users()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_user()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

# Global
db_config = get_valid_db_config()
setup_database_and_table(db_config)

if __name__ == "__main__":
    menu()
