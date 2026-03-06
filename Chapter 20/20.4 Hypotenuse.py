'''
Given two numbers that represent the lengths of a right triangle's legs (sides adjacent to the right angle), output the length of the third side (i.e. hypotenuse) with two digits after the decimal point. The formula to calculate the hypotenuse is called Pythagorean's Theorem, as shown:

c = sq((a,2) + (b,2))
Where a and b are the legs of the right triangle and c is the hypotenuse.

Note: To output the length of the hypotenuse with two digits after the decimal point, use:
print(f'Hypotenuse is {side3:.2f}'), where side3 is the variable representing the length of the hypotenuse.

Ex: If the input is:
    3.00
    4.00

the output is:
    Right triangle has side lengths 3.00 and 4.00
    Hypotenuse is 5.00
'''
import math

a = float(input())
b = float(input())

side3 = math.sqrt(math.pow(a,2) + math.pow(b,2))

print(f'Right triangle has side lengths {a:.2f} and {b:.2f}')
print(f'Hypotenuse is {side3:.2f}')