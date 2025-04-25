# import random

# def get_computer_choice():
#     return random.choice(["snake", "water", "gun"])

# def check_winner(player, computer):
#     if player == computer:
#         return "It's a tie!"

#     if player == "snake":
#         if computer == "water":
#             return "You win! Snake drinks the water."
#         elif computer == "gun":
#             return "You lose! Gun shoots the snake."

#     elif player == "water":
#         if computer == "gun":
#             return "You win! Water drowns the gun."
#         elif computer == "snake":
#             return "You lose! Snake drinks the water."

#     elif player == "gun":
#         if computer == "snake":
#             return "You win! Gun shoots the snake."
#         elif computer == "water":
#             return "You lose! Water drowns the gun."

#     return "Invalid input."

# def main():
#     print("Welcome to Snake Water Gun Game!")
#     print("Choices: snake, water, gun")
#     player_choice = input("Enter your choice: ").lower()

#     if player_choice not in ["snake", "water", "gun"]:
#         print("Invalid choice. Please select from snake, water, or gun.")
#         return

#     computer_choice = get_computer_choice()
#     print(f"Computer chose: {computer_choice}")
#     result = check_winner(player_choice, computer_choice)
#     print(result)

# if __name__ == "__main__":
#     main()


import random

def check(comp, user):
  if comp ==user:
    return 0
    
  if(comp == 0 and user ==1):
    return -1
    
  if(comp == 1 and user ==2):
    return -1
    
  if(comp == 2 and user == 0):
    return -1

  return 1
    
  
comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")
  



