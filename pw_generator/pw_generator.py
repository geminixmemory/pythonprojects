# This program serves as a password generator, which the user can specify
# 1. the length of the password, and
# 2. whether to involve special char or not 

import string
import random

pw_length = int(input("How long do you want yr PW? "))
pw = []
special_char = input("Does the PW contain special char? Y/N ")
special_char = special_char.strip()

if special_char.lower() == "y":
    for x in range(pw_length):
        # weight the probability of alphabets, digits & special char to 55%, 30% & 15%
        char_type = random.randint(1, 100)
        if char_type < 56:
            pw.append(random.choice(string.ascii_letters))
        elif 56 <= char_type <= 85:
            pw.append(str(random.randint(0, 9)))
        else:
            pw.append(random.choice(string.punctuation))

elif special_char.lower() == "n":
    for x in range(pw_length):
        # weight the probability of alphabets & digits to 60% & 40%
        char_type = random.randint(1, 10)
        if char_type < 7:
            pw.append(random.choice(string.ascii_letters))
        else:
            pw.append(str(random.randint(0, 9)))   
            
else:
    raise ValueError("Only Y or N allowed ")

print(f"Here you go! Your newly generated password is '{"".join(pw)}'")    


