# 40 Day40 - Exercise 4
def encode(word):
    if len(word) > 3:
        word_list = list(word)
        first_letter = word_list.pop(0)
        word_list.append(first_letter)
        word_core = "".join(word_list)
        prefix = random.choice(string.ascii_letters) * 3
        suffix = random.choice(string.ascii_letters) * 3
        return prefix + word_core + suffix
    else:
        word_list = list(word)
        word_list.reverse()
        return "".join(word_list)

def decode(encoded):
    if len(encoded) > 3:
        core_list = list(encoded[3:-3])
        last_letter = core_list.pop()
        core_list.insert(0, last_letter)
        return "".join(core_list)
    else:
        word_list = list(encoded)
        word_list.reverse()
        return "".join(word_list)

print("Welcome to the Language Encoder and Decoder!")
action = input("Do you want to encode or decode? (e/d): ").strip().lower()

if action == 'e':
    word = input("Enter a word to encode: ")
    encoded_word = encode(word)
    print("Encoded word is:", encoded_word)
elif action == 'd':
    word = input("Enter a word to decode: ")
    decoded_word = decode(word)
    print("Decoded word is:", decoded_word)
else:
    print("Invalid choice! Please enter 'e' to encode or 'd' to decode.")