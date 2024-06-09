# This program checks whether an input string is a palindrome

word = input("Pls gimme a word to check if it is a palindrome ")
separ = round(len(word) / 2)

for x in range(0, separ):
    y = word[(x + 1) * -1]
    if word[x] != y:
        exit("This is not a palindrome")
        
print("Your input string is a palindrome")