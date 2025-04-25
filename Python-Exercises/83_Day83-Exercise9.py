import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# List of names
l = ["Dharmik", "Sarman", "Keyur"]

# Loop through the list and pronounce each name
for name in l:
    message = f"Hello {name} how are you?"
    print(message)
    engine.say(message)
    engine.runAndWait()
