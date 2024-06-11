# This program ask the user to input a sentence & then reverse the string order within

sentence = input("Pls input a sentence for testing \n")

list = sentence.split(" ")
new_list = []
new_list.append(list[-1])

for x in range(2, len(list) + 1):
    y = x * -1
    new_list.append(list[y])

print(" ".join(new_list))