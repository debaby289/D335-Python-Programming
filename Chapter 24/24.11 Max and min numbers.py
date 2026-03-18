'''
Write a program whose inputs are four integers, and whose outputs are the maximum and the minimum of the four values.

Ex: If the input is:
    12
    18
    4
    9
the output is:
    Maximum is 18 
    Minimum is 4

The program must define and call the following two functions. Define a function named max_number() that takes four integer parameters and returns an integer representing the maximum of the four integers. Define a function named min_number() that takes four integer parameters and returns an integer representing the minimum of the four integers.
    def max_number(num1, num2, num3, num4)
    def min_number(num1, num2, num3, num4)

Note: DO NOT use max() and min().
'''
def max_number(num1, num2, num3, num4):
    max_num = num1

    if max_num < num2:
        max_num = num2

    if max_num < num3:
        max_num = num3

    if max_num < num4:
        max_num = num4

    return max_num
    
def min_number(num1, num2, num3, num4):
    min_num = num1

    if min_num > num2:
        min_num = num2

    if min_num > num3:
        min_num = num3

    if min_num > num4:
        min_num = num4

    return min_num
    
    
if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())

    print(f'Maximum is {max_number(num1, num2, num3, num4)}')
    print(f'Minimum is {min_number(num1, num2, num3, num4)}')