# String Slicing, Methods, and Formatting Example

def main():
    original_string = "  Hello, Python Developer!  "

    print("Original String:")
    print(f"'{original_string}'\n")

    # --- STRING SLICING ---
    print("String Slicing Examples:")
    print("==================================================================================")
    print(f"First 5 characters: '{original_string[:5]}'")
    print(f"Last 10 characters: '{original_string[-10:]}'")
    print(f"Characters from index 2 to 10: '{original_string[2:11]}'")
    print(f"Every second character: '{original_string[::2]}'\n")

    # --- STRING METHODS ---
    trimmed = original_string.strip()  # removes leading/trailing spaces
    uppercased = trimmed.upper()
    lowercased = trimmed.lower()
    replaced = trimmed.replace("Developer", "Engineer")
    title_case = trimmed.title()
    word_list = trimmed.split()

    print("String Method Examples:")
    print("==================================================================================")
    print(f"Trimmed string: '{trimmed}'")
    print(f"Uppercased: '{uppercased}'")
    print(f"Lowercased: '{lowercased}'")
    print(f"Replaced 'Developer' with 'Engineer': '{replaced}'")
    print(f"Title Case: '{title_case}'")
    print(f"Split into words: {word_list}")
    print(f"Does string start with 'Hello'? {'Yes' if trimmed.startswith('Hello') else 'No'}")
    print(f"Does string end with 'Developer!'? {'Yes' if trimmed.endswith('Developer!') else 'No'}\n")

    # --- STRING FORMATTING ---
    name = "Dharmik"
    role = "Python Developer"
    years_exp = 1.5

    print("String Formatting Examples:")
    print("==================================================================================")
    print("Hello {}, your role is {}.".format(name, role))
    print(f"{name} has {years_exp:.1f} years of experience as a {role}.")
    print("Welcome, %s! You are working as a %s." % (name, role))


if __name__ == "__main__":
    main()
