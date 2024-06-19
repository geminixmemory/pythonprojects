# This program prints specified quantity of Fibonacci nos, according to the user's instruction

num_qty = int(input("Pls enter the quantity of Fibonacci numbers you want "))

def comput(a):
    fibo_list = []
    orig_num = 1
    new_num = 0
    for x in range(a):
        fibo_list.append(orig_num)
        new_num = orig_num + new_num
        orig_num = new_num
    return fibo_list
        
print(comput(num_qty))
