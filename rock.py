import random

options = ["rock", "paper", "scissors"]

user_choice = input("choose rock, paper, or scissors: ")

computer_choice = random.choice(options)

print("you chose:", user_choice)
print("computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
    
else:
    print("you lose!")
