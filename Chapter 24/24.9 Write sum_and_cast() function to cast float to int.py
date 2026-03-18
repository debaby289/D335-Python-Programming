'''
Complete the sum_and_cast() function that casts the parameters from floats to integers and returns the resulting sum.
Note that the returned value of the sum_and_cast() function is printed.

Ex: If the float values are 14.2 and 19.9, then the output is:
    33

Ex: If the float values are 2.5 and 3.1, then the output is:
    5
'''
import math

def sum_and_cast(d1, d2):
    return int(d1) + int(d2)

if __name__ == '__main__':
    print(sum_and_cast(14.2, 19.9))
    print(sum_and_cast(2.5, 3.1))