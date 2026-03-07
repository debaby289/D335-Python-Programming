'''
Write a program that takes an integer (0 - 9999) as input and outputs the number of digits.

Ex: If the input is:
    7493
the output is:
    4 digits

Ex: If the input is:
    7
the output is:
    1 digit
'''
user_input = input()

numb_len = len(user_input)

if numb_len == 1:
    print(f'{numb_len} digit')
else:
    print(f'{numb_len} digits')