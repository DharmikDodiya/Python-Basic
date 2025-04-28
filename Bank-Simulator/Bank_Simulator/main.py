from bank_account import BankAccountManager
from getpass import getpass

def menu():
    print("\n--- Bank Simulator APP ---")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Delete Account")
    print("6. Exit")

def run():
    bank = BankAccountManager()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter account holder name: ")
            amount = float(input("Enter amount to initial deposit: ").isdigit())
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            while True:
                pin = getpass("Enter your 4-6 digit numeric PIN: ")
                if not pin.isdigit():
                    print("PIN must be numeric.")
                elif not (4 <= len(pin) <= 6):
                    print("PIN must be between 4 to 6 digits.")
                else:
                    break
            
            bank.create_account(name, pin, amount)

        elif choice == "2":
            acc_num = input("Enter account number: ")
            pin = getpass("Enter your PIN: ")
            bank.show_account(acc_num, pin)

        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            pin = getpass("Enter your PIN: ")
            bank.deposit(acc_num, amount, pin)

        elif choice == "4":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            pin = getpass("Enter your PIN: ")
            bank.withdraw(acc_num, amount, pin)

        elif choice == "5":
            acc_num = input("Enter account number to delete: ")
            pin = getpass("Enter your PIN: ")
            bank.delete_account(acc_num, pin)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run()
