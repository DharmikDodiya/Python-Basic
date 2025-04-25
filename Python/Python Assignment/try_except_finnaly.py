# Custom exception
class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Function that performs division
def divide_numbers(num1, num2):
    try:
        # Check if inputs are valid numbers
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise InvalidInputError("Both inputs must be numbers.")
        
        # Check for division by zero
        result = num1 / num2
        
    except InvalidInputError as e:
        # Handle invalid input exception
        print(f"Custom Exception: {e}")
    except ZeroDivisionError:
        # Handle division by zero exception
        print("Error: Cannot divide by zero.")
    except Exception as e:
        # Handle other generic exceptions
        print(f"An unexpected error occurred: {e}")
    else:
        # This block runs if no exceptions were raised
        print(f"Result: {result}")
    finally:
        # This block will run no matter what
        print("Execution completed.")

# Test cases
print("Test 1:")
divide_numbers(10, 2)  # Valid division

print("\nTest 2:")
divide_numbers(10, 0)  # Division by zero

print("\nTest 3:")
divide_numbers("ten", 2)  # Invalid input (string instead of a number)

print("\nTest 4:")
divide_numbers(10, "two")  # Invalid input (string instead of a number)
