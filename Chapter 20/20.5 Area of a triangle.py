'''
Using Heron's formula, you can calculate the area of a triangle if you know the lengths of all three sides. Given the length of each side of a triangle as input, calculate the area of the triangle using Heron's formula as follows:
    s = half of the triangle's perimeter
    area = the square root of s*(s-a)*(s-b)*(s-c), where a, b, and c are each sides of the triangle.
Hint: Use the sqrt() function from the math module to calculate the square root.

Output the floating-point value of the area with two digits after the decimal point using the following statement:
print(f'Triangle area = {your_value:.2f}')

Ex: If the input for a, b, and c is:


    3.0
    4.0
    5.0

the output is:
    Triangle area = 6.00
'''
import math

a = float(input())
b = float(input())
c = float(input())

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f'Triangle area = {area:.2f}')