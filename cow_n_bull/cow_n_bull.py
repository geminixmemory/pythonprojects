""" This game guess a randomly generated 4-digit number by computer, 
    for each correct number + position 1 cow,
    for each correct number only 1 bull,
    guess all correct to finish the game
"""
import random

def main():
    # computer generated a 4-digit number as the answer for each game
    ans = random.randint(1000, 9999)
    # break down the 4 digits into a list for reconciliation
    ans_list = []
    for x in str(ans):
        ans_list.append(x)
    print(ans)
    
    guess = input("Please take a guess of the 4-digit number ")
    counter = 1
    while int(guess) != ans:
        # trigger the function to form a guess list
        try_list = conver_guess(guess)
        temp_ans = ans_list.copy() # ensure every new try is refreshed
        cow, bull = one_turn(temp_ans, try_list)
        print(f"You have got {cow}🐄 and {bull}🐂 for this turn ")
        conti = input("Want to try again? Y/N ")
        if conti.lower() == "y":
            guess = input("Please take a guess of the 4-digit number ")  
        elif conti.lower() == "n":
            exit("Goodbye! ") 
        else:
            raise ValueError("Only Y/N allowed, man >.< ") 
        counter += 1
            
    print(f"You Win!! The answer is {ans}, after {counter} times of trial ^^. ") 
   
# This function convert the guess number into a list to reconcile with the answer            
def conver_guess(guess):
    guess_list = []
    for y in guess:
        guess_list.append(y)
    return guess_list        
    
def one_turn(list, guess_list):
    cow = 0
    bull = 0
    for z in range(4):
        if guess_list[z] == list[z]:
            cow += 1
            list[z] = "None"
        elif guess_list[z] in list:
            bull += 1
            # 1st take the guess_list[z] value
            # 2nd compute the position of list inside []
            # 3rd spot the value of list[position] & convert
            list[list.index(guess_list[z])] = "None"
    return cow, bull 
    
if __name__ == "__main__":
    main()