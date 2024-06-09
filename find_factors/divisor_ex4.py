# This program digs out all factors of an input number, except 1 and itself

num = int(input("Pls provide a num to check on its factors or divisors "))

# 1st set up a range for later looping to dig out the factors
chk_list = range(2, num - 1)
factor = []

for x in chk_list:
    if num % x == 0:
        factor.append(x)

factor.sort()
print(factor)

# my_range = range(11, 87616, 4)
# print(my_range[154])
# formula ==>> range[154] = 11 + 4*154
