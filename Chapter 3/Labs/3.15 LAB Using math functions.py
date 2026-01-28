'''
Docstring for Chapter 3.Labs.3.15.1: LAB: Using math functions
Given three floating-point numbers x, y, and z, output x to the power of z, x to the power of (y to the power of z), the absolute value of (x minus y), and the square root of (x to the power of z).

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')

Ex: If the input is:
5.0
1.5
3.2

Then the output is:
172.47 361.66 3.50 13.13
'''
import math

user_x = float(input())
y = float(input())
z = float(input())
x = int()

#output x to the power of z
x = math.pow(user_x,z)
print(f'{x:.2f}',end=' ')

#x to the of (y to the power of z)
x = math.pow(user_x,(math.pow(y,z)))
print(f'{x:.2f}',end=' ')

#absolute value of x - y
x = math.fabs(user_x - y)
print(f'{x:.2f}',end=' ')

#square root of (x to z)
x = math.sqrt(math.pow(user_x,z))
print(f'{x:.2f}')