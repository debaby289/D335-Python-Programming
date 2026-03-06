'''
The volume and area of a cylinder are calculated as:
    Volume = πr2h
    Area =  2πrh + 2πr2

Given the radius and height of a cylinder as floating-point numbers, output the volume and area of the cylinder.

Hint: Use the built-in pow() function and the constant pi from the math module in your calculations.

Output each floating-point value with two digits after the decimal point using the following statement:
print(f'Volume (cubic inches): {yourValue:.2f}')

Ex: If the input is:
    5.2
    8.1

where 5.2 is the radius of the cylinder and 8.1 is the height of the cylinder, then the output is:
    Volume (cubic inches): 688.08
    Surface area (square inches): 434.55
'''
import math

radius = float(input())
height = float(input())

volume = math.pi * (math.pow(radius,2)) * height
area = (2 * math.pi * radius * height) + (2 * math.pi * math.pow(radius,2))

print(f'Volume (cubic inches): {volume:.2f}')
print(f'Surface area (square inches): {area:.2f}')