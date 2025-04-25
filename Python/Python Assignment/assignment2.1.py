import re
from tabulate import tabulate

def show_details(data):
    table_data = []
    table_data = [
    [cid, info['name'], info['email'], ", ".join(info['phones'])]
    for cid, info in contact_manager.items()
    ]    
    print(tabulate(table_data, headers=["ID", "Name", "Email", "Phones"], tablefmt="grid"))

# ------------------- PART 1: From JSON -------------------

# Contact Manager (Dictionary Based)
contact_manager = {}

# Simulated complex JSON input
data = {
    "contacts": [
        {
            "id": 1,
            "personal_info": {
                "name": "Alice",
                "email": "alice@example.com"
            },
            "phones": ["1234567890", "9876543210"]
        },
        {
            "id": 2,
            "personal_info": {
                "name": "Bob",
                "email": "bob@example.com"
            },
            "phones": ["5555555555"]
        }
    ],
    "meta": {
        "count": 2,
        "source": "imported"
    }
}

# Destructuring and populating contact manager
for contact in data['contacts']:
    contact_id = contact['id']
    name = contact['personal_info']['name']
    email = contact['personal_info']['email']
    phones = contact['phones']

    contact_manager[contact_id] = {
        'name': name,
        'email': email,
        'phones': phones
    }

# Display contacts from JSON in table
print("---------------------------------------------------------------------------------------------")
print("Contact List from JSON (Tabular Format)")
print("---------------------------------------------------------------------------------------------")
# table_data = [
#     [cid, info['name'], info['email'], ", ".join(info['phones'])]
#     for cid, info in contact_manager.items()
# ]
# print(tabulate(table_data, headers=["ID", "Name", "Email", "Phones"], tablefmt="grid"))
show_details(contact_manager.items())

# ------------------- PART 2: User Input -------------------

print("\n---------------------------------------------------------------------------------------------")
print("Contact List Using User Inputs")
print("---------------------------------------------------------------------------------------------")

# Email Validation Function
def is_valid_email(email):
    # Simple email regex for validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

# Name Validation Function
def is_valid_name(name):
    # Allow alphabetic characters and spaces
    return all(part.isalpha() for part in name.split())


contact_manager = {}
contact_count = int(input("How many contacts do you want to add? "))

for i in range(contact_count):
    print(f"\nEnter details for Contact #{i + 1}")
    contact_id = i + 1

    # Validate name format (only alphabetic characters)
    while True:
        name = input("Name: ")
        if is_valid_name(name):
            break
        else:
            print("Invalid name. Please enter a name containing only alphabetic characters.")

    # Validate email format
    while True:
        email = input("Email: ")
        if is_valid_email(email):
            break
        else:
            print("Invalid email. Please enter a valid email address.")

    phones = []
    phone_count = int(input("How many phone numbers for this contact? "))
    for j in range(phone_count):
        while True:
            phone = input(f"Enter phone number #{j + 1}: ")
            if phone.isdigit() and 10 <= len(phone) <= 15:
                phones.append(phone)
                break
            else:
                print("Invalid phone number. Please enter only digits (10 to 15 digits).")

    contact_manager[contact_id] = {
        'name': name,
        'email': email,
        'phones': phones
    }

# Display user input contacts in table
print("\nContact List (User Inputs in Tabular Format)")
# table_data = [
#     [cid, info['name'], info['email'], ", ".join(info['phones'])]
#     for cid, info in contact_manager.items()
# ]
# print(tabulate(table_data, headers=["ID", "Name", "Email", "Phones"], tablefmt="grid"))
show_details(contact_manager.items())
