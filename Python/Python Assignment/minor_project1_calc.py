# import re

# # Simple Calculator: Build a CLI-based calculator that supports basic arithmetic operations and handles invalid input gracefully
# print("Calculator Application")
# print("---------------------")

# # Function to perform arithmetic operations
# def calculate(num1, operator, num2):
#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "%":
#         print('call')
#         return num1 % num2
#     elif operator == "/":
#         if num2 != 0:
#             return num1 / num2
#         else:
#             return "Error: Division by zero"
#     else:
#         return "Error: Invalid operator"

# # Function to validate user input
# def is_valid_input(input_str):
#     pattern = r"^\s*(\d+(?:\.\d+)?)\s*([+\-*/])\s*(\d+(?:\.\d+)?)\s*$"
#     return re.match(pattern, input_str)

# # Menu
# def menu():
#     while True:
#         print("\n======= User CRUD Menu =======")
#         print("1. Addition")
#         print("2. Subtraction")
#         print("3. Multiply")
#         print("4. Division")
#         print("5. Percent")
#         print("6. Exit")

#         choice = input("Choose an operation (1-6): ")

#         if choice == "1":
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#             result = calculate(num1, "+", num2)
#             print("Result:", result)
#         elif choice == "2":
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#             result = calculate(num1, "-", num2)
#             print("Result:", result)
#         elif choice == "3":
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#             result = calculate(num1, "*", num2)
#             print("Result:", result)
#         elif choice == "4":
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#             result = calculate(num1, "/", num2)
#             print("Result:", result)
#         elif choice == "5":
#             num1 = float(input("Enter first number: "))
#             num2 = float(input("Enter second number: "))
#             print("call")
#             result = calculate(num1, "%", num2)
#             print("Result:", result)
#         elif choice == "6":
#             print("Exiting program. Bye!")
#             break
#         else:
#             print("Invalid choice. Try again.")

# if __name__ == "__main__":
#     menu()


# Develop a CLI-based calculator that supports basic arithmetic operations with user input validation and handles invalid input gracefully
def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "%":
        return num1 % num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_operator():
    operator = input("Enter operator (+, -, *, /, %): ").strip()
    if operator in ["+", "-", "*", "/", "%"]:
        return operator
    elif operator == "":
        print("No operator entered, defaulting to '+'")
        return "+"
    else:
        print("Invalid operator. Defaulting to '+'")
        return "+"

def menu():
    print("Calculator Application")
    print("----------------------")

    while True:
        print("\n======= Calculator Menu =======")
        print("1. Calculate")
        print("2. Exit")

        choice = input("Choose an option (1-2): ")

        if choice == "1":
            num1 = get_number("Enter the first number: ")
            operator = get_operator()
            num2 = get_number("Enter the second number: ")

            result = calculate(num1, operator, num2)
            print(f"Result: {result}")
        elif choice == "2":
            print("Exiting program. Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()

