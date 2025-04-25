from tabulate import tabulate
import re

# In-memory user list
users = []

# CRUD Functions

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def createUser():
    name = input("Enter name: ")
    while True:
        email = input("Enter email: ")
        if is_valid_email(email):
            break
        print("Invalid email format. Try again.")
    user_id = len(users) + 1
    users.append({"id": user_id, "name": name, "email": email})
    print(f"User created with ID: {user_id}")

def getAllUsers():
    if not users:
        print("No users found.")
    else:
        print("\n All Users:")
        print(tabulate(users, headers="keys", tablefmt="grid"))

def getUser():
    user_id = int(input("Enter user ID to fetch: "))
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        print("\n👤 User Info:")
        print(tabulate([user], headers="keys", tablefmt="grid"))
    else:
        print("User not found.")

def updateUser():
    user_id = int(input("Enter user ID to update: "))
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        name = input("Enter new name (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        if name:
            user["name"] = name
        if email:
            if is_valid_email(email):
                user["email"] = email
            else:
                print("Invalid email format. Email not updated.")
        print("User updated:")
        print(tabulate([user], headers="keys", tablefmt="grid"))
    else:
        print("User not found.")

def deleteUser():
    global users
    user_id = int(input("Enter user ID to delete: "))
    before_count = len(users)
    users = [u for u in users if u["id"] != user_id]
    after_count = len(users)
    if before_count != after_count:
        print("User deleted.")
    else:
        print("User not found.")

# Menu
def menu():
    while True:
        print("\n======= User CRUD Menu =======")
        print("1. Create User")
        print("2. View All Users")
        print("3. View Single User")
        print("4. Update User")
        print("5. Delete User")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            createUser()
        elif choice == "2":
            getAllUsers()
        elif choice == "3":
            getUser()
        elif choice == "4":
            updateUser()
        elif choice == "5":
            deleteUser()
        elif choice == "6":
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
