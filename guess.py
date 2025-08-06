import random 
playing = True
number = (random.randint(10,20))

print("heyy lets play. I will generate a number from 10 to 20 and you will have to guess the number , remmember one digit at one time")

while playing:
    guess = (input("give me your best guess!!! \n"))
    if number == guess:
        print("you guessed it right, You win the game")
        print("the number was ", number)
        break
    else:
        print("you guess is wrong, try again.\n")