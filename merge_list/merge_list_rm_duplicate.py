# This program merges 2 lists & removes duplicate values within 

a = [1, 1, 2, 3, 5, 8, 13, 21, 55, 89, 34, 68]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
 
for x in a:
    b.append(x)
     
c = set(b)  
# the result is in DICT format, or list(set()) to yield the list format

print(c)
    