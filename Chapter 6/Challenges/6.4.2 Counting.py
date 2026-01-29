'''
Challenge : Counting
Level 1
Integer user_num is read from input. Integer i is initialized with 24. Complete the while loop to perform the following tasks at each iteration until i is less than user_num:
    Decrement i.
    If i is divisible by 2, then output the value of i.
'''
user_num = int(input())
i = 24

while i >= user_num:
    i -= 1
    if i % 2 == 0:
        print(i)

'''
Level 2
Integer input_num is read from input. Initialize variable k with 41. Then, write a while loop to perform the following tasks at each iteration until k is less than input_num:
    Decrement k.
    If k is divisible by 3, then output the value of k.
'''
input_num = int(input())
k = 41

while k >= input_num:
    k -= 1
    if k % 3 == 0:
        print(k)