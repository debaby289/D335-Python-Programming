'''
Docstring for Chapter 9.Labs.9.20 Filter and sort a list
Write a program that gets a list of integers from input, and outputs negative integers in descending order (highest to lowest).
Ex: If the input is:
10 -7 4 -39 -6 12 -2
the output is:
-2 -6 -7 -39 
For coding simplicity, follow every output value by a space. Do not end with newline.
'''
my_list = []

user_input = input()

for user in user_input.split():
    if int(user) < 0:
        my_list.append(int(user))  
sorted_list = sorted(my_list, reverse=True)  
for num in sorted_list:
    print(num, end=' ')  