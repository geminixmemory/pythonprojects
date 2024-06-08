""" This program asks the user to input both a numerator & 
    a denominator, then check if they are dividable, PLUS
    to identify whether the numerator is an odd or even number, PLUS
    whether it is a multiple of 4 or not, so useful ^_^  
"""

num = int(input("Pls write a num for dissecting: "))
check = int(input("Then gimme a num for division: "))
if num % 4 == 0 and num % check == 0:
    print("Great!! It is both a multiple of 4 & dividable by yr num!!")
elif num % check == 0:
    print("It can be divided by yr num, but not a multiple of 4, not too bad!!")
elif num % 4 == 0:
    print("It is a multiple of 4 only, still OK!!")
elif num % 2 == 0:
    print("It is an even number, O well!! ")
else:
    print("Nope, not dividable at all, just an odd num... ")