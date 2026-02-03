'''
Challenge : Functions with parameters and return values
Level 1
Define a function compute_result() that has one parameter and returns the parameter minus 5.1.

Ex: If the input is 6.9, then the output is:
1.80
'''
def compute_result(parameter):
    parameter = parameter - 5.1
    return parameter

user_input = float(input())
print(f'{compute_result(user_input):.2f}')
'''
Level 2
Define a function calc_num() that has two parameters and returns the sum of the two parameters minus 7.

Ex: If the input is:
5
8

then the output is:
6
'''
def calc_num(x,y):
    sum = (x + y) - 7
    return sum

num_in1 = int(input())
num_in2 = int(input())

print(calc_num(num_in1, num_in2))