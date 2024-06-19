# This number guessing game first has the system randomly generated a number between 1 to 9
# The player / user is then asked to guess the number
# The program offers feedback / hints as the player guesses along, either too big or too small
# Upon the correct guess, the program will count how many time the player has tried &
# the player can always exit the game via a clear y/n instruction 

import random

ans = random.randint(1, 9)
guess = input("Take a guess of a num between 1 - 9 \n")
counter = 1

while int(guess) != ans:
    counter += 1
    if int(guess) > ans:
        print("Nope, your guess is too large")
    else:
        print("Nope, your guess is too small")
    guess = input("Take a guess again or type in 'exit' to quit the game \n")
    if guess == "exit":
        exit("Goodbye! ")
    elif not guess.isdigit():
        raise ValueError("Either an integer input or 'exit' only. ")
    
print(f"Wow, amazing!!!  You have got the correct answer, which is {ans}")
print(f"after {counter} time(s) of trial.")
        

