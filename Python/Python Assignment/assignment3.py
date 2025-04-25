# Using Dynamic database connection creation and table creation using MySQL, Fernet encryption/decryption and tabulate library to perform CRUD operations

import mysql.connector
import os
import json
from mysql.connector import Error
from tabulate import tabulate
from cryptography.fernet import Fernet
from getpass import getpass

SECRET_KEY_FILE = "creds/secret.key"
CONFIG_FILE = "creds/db_config.json"
# DB_NAME = "library_db"
# TABLE_NAME = "books"


def load_or_create_secret_key():
    if os.path.exists(SECRET_KEY_FILE):
        with open(SECRET_KEY_FILE, 'rb') as f:
            return f.read()
    key = Fernet.generate_key()
    os.makedirs(os.path.dirname(SECRET_KEY_FILE), exist_ok=True)
    with open(SECRET_KEY_FILE, 'wb') as f:
        f.write(key)
    return key


def get_or_create_db_config():
    key = load_or_create_secret_key()
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
    db_name = required_input("Enter Database Name (e.g., library_db): ") or "library_db"
    table_name = required_input("Enter Table Name (e.g., books): ") or "books"

    config = {"host": host, "user": user, "password": password, "db_name": db_name, "table_name": table_name}
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    encrypted_config = fernet.encrypt(json.dumps(config).encode())
    with open(CONFIG_FILE, 'wb') as f:
        f.write(encrypted_config)

    return config


def setup_library_database(config):
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"]
        )
        db_name = config["db_name"]
        table_name = config["table_name"]

        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute(f"USE {db_name}")
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL
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


def get_valid_db_config():
    attempt = 0
    while True:
        config = get_or_create_db_config()
        success, db_name, table_name = setup_library_database(config)
        if success:
            return config, db_name, table_name
        else:
            attempt += 1
            if os.path.exists(CONFIG_FILE):
                os.remove(CONFIG_FILE)
            print(f"\nAttempt {attempt}: Invalid credentials. Please try again...\n")

db_config, DB_NAME, TABLE_NAME = get_valid_db_config()

def connect_db():
    return mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database=DB_NAME
    )

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(f"INSERT INTO {TABLE_NAME} (title, author) VALUES (%s, %s)", (title, author))
        conn.commit()
        print("Book added successfully!")
    except Error as e:
        print("Error adding book:", e)
    finally:
        cursor.close()
        conn.close()

def view_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    books = cursor.fetchall()
    if books:
        print("\n--- All Books ---")
        print(tabulate(books, headers=["ID", "Title", "Author"], tablefmt="grid"))
    else:
        print("No books found.")
    cursor.close()
    conn.close()


def search_books():
    keyword = input("Enter title keyword to search: ").strip()
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {TABLE_NAME} WHERE title LIKE %s", (f"%{keyword}%",))
        results = cursor.fetchall()
        if results:
            print("\n--- Search Results ---")
            print(tabulate(results, headers=["ID", "Title", "Author"], tablefmt="grid"))
        else:
            print("No matching books found.")
    except Error as e:
        print("Search error:", e)
    finally:
        cursor.close()
        conn.close()


def delete_book():
    book_id = input("Enter book ID to delete: ").strip()
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = %s", (book_id,))
        conn.commit()
        if cursor.rowcount > 0:
            print("Book deleted successfully!")
        else:
            print("No book found with the given ID.")
    except Error as e:
        print("Error deleting book:", e)
    finally:
        cursor.close()
        conn.close()

def update_book():
    book_id = input("Enter book ID to update: ").strip()
    title = input("Enter new title: ").strip()
    author = input("Enter new author: ").strip()

    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(f"UPDATE {TABLE_NAME} SET title = %s, author = %s WHERE id = %s", (title, author, book_id))
        conn.commit()
        if cursor.rowcount > 0:
            print("Book updated successfully!")
        else:
            print("No book found with the given ID.")
    except Error as e:
        print("Error updating book:", e)
    finally:
        cursor.close()
        conn.close()

def library_menu():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book by Title")
        print("4. Delete Book")
        print("5. Update Book")
        print("6. Exit")

        choice = input("Enter choice: ").strip()
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_books()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            update_book()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    library_menu()

# Using static database connection in a class

# import mysql.connector
# from mysql.connector import Error
# from tabulate import tabulate


# class LibrarySystem:
#     def __init__(self, host, user, password, database):
#         self.host = host
#         self.user = user
#         self.password = password
#         self.database = database
#         self.connection = None
#         self.cursor = None

#         if self._ensure_database():
#             self._connect_to_database()
#             if self.connection and self.connection.is_connected():
#                 self._create_books_table()

#     def _ensure_database(self):
#         try:
#             temp_conn = mysql.connector.connect(
#                 host=self.host,
#                 user=self.user,
#                 password=self.password
#             )
#             temp_cursor = temp_conn.cursor()
#             temp_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
#             print(f"Database '{self.database}' is ready.")
#             temp_cursor.close()
#             temp_conn.close()
#             return True
#         except Error as e:
#             print(f"Error creating database: {e}")
#             return False

#     def _connect_to_database(self):
#         try:
#             self.connection = mysql.connector.connect(
#                 host=self.host,
#                 user=self.user,
#                 password=self.password,
#                 database=self.database
#             )
#             if self.connection.is_connected():
#                 print("Connected to database.")
#                 self.cursor = self.connection.cursor()
#         except Error as e:
#             print(f"Error connecting to database: {e}")
#             self.connection = None
#             self.cursor = None

#     def _create_books_table(self):
#         try:
#             query = """
#             CREATE TABLE IF NOT EXISTS books (
#                 id INT AUTO_INCREMENT PRIMARY KEY,
#                 title VARCHAR(255) NOT NULL,
#                 author VARCHAR(255) NOT NULL
#             );
#             """
#             self.cursor.execute(query)
#             self.connection.commit()
#             print("Table 'books' is ready.")
#         except Error as e:
#             print(f"Error creating table: {e}")

#     def add_book(self, title, author):
#         if not self.cursor:
#             print("Cannot add book: No database connection.")
#             return
#         try:
#             query = "INSERT INTO books (title, author) VALUES (%s, %s)"
#             self.cursor.execute(query, (title, author))
#             self.connection.commit()
#             print(f"Book '{title}' added.")
#         except Error as e:
#             print(f"Failed to add book: {e}")

#     def remove_book(self, id):
#         if not self.cursor:
#             print("Cannot remove book: No database connection.")
#             return
#         try:
#             query = "DELETE FROM books WHERE id = %s"
#             self.cursor.execute(query, (id,))
#             self.connection.commit()
#             if self.cursor.rowcount > 0:
#                 print(f"Book with ID '{id}' removed.")
#             else:
#                 print(f"Book with ID '{id}' not found.")
#         except Error as e:
#             print(f"Failed to remove book: {e}")

#     def search_by_title(self, keyword):
#         if not self.cursor:
#             print("Cannot search: No database connection.")
#             return []
#         try:
#             query = "SELECT title, author FROM books WHERE title LIKE %s"
#             self.cursor.execute(query, (f"%{keyword}%",))
#             rows = self.cursor.fetchall()
#             if rows:
#                 print("\n Searched Books in Library:")
#                 print(tabulate(rows, headers=["ID", "Title", "Author"], tablefmt="grid"))
#             else:
#                 print("No books in the library.")
#         except Error as e:
#             print(f"Search failed: {e}")
#             return []

#     def show_all_books(self):
#         if not self.cursor:
#             print("Cannot show books: No database connection.")
#             return
#         try:
#             query = "SELECT id, title, author FROM books"
#             self.cursor.execute(query)
#             rows = self.cursor.fetchall()
#             if rows:
#                 print("\n All Books in Library:")
#                 print(tabulate(rows, headers=["ID", "Title", "Author"], tablefmt="grid"))
#             else:
#                 print("No books in the library.")
#         except Error as e:
#             print(f"Failed to fetch books: {e}")

#     def close(self):
#         if self.connection and self.connection.is_connected():
#             self.cursor.close()
#             self.connection.close()
#             print("Connection closed.")


# def main():
#     library = LibrarySystem(
#         host="localhost",
#         user="root",
#         password="password",
#         database="library_db"
#     )

#     if not library.connection:
#         print("Exiting: Could not initialize database.")
#         return

#     while True:
#         print("\n=== Library Menu ===")
#         print("1. Add Book")
#         print("2. Remove Book")
#         print("3. Search Book by Title")
#         print("4. Show All Books")
#         print("5. Exit")


#         choice = input("Enter your choice (1-5): ").strip()

#         if choice == "1":
#             title = input("Enter book title: ").strip()
#             author = input("Enter author name: ").strip()
#             library.add_book(title, author)

#         elif choice == "2":
#             id = input("Enter book id to remove: ").strip()
#             library.remove_book(id)

#         elif choice == "3":
#             keyword = input("Enter title keyword to search: ").strip()
#             results = library.search_by_title(keyword)
#             if results:
#                 print("\nSearch Results:")
#                 for title, author in results:
#                     print(f"• {title} by {author}")
#             else:
#                 print("No books found.")

#         elif choice == "4":
#             library.show_all_books()

#         elif choice == "5":
#             print("Exiting... Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please enter a number between 1 and 5.")

#     library.close()


# if __name__ == "__main__":
#     main()
