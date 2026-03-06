'''
Given a floating-point number as input, output the square root of the given number. Use the appropriate function from the math module to perform the operation.

Output each floating-point value with two digits after the decimal point using the following statement:
print(f'Square root of {value1:.2f} = {value2:.2f}'), where value1 and value2 are floating-point values.

Ex: If the input is:
    9.0

the output is:
    Square root of 9.00 = 3.00
'''
import math

squared = float(input())
square_root = math.sqrt(squared)

print(f'Square root of {squared:.2f} = {square_root:.2f}')