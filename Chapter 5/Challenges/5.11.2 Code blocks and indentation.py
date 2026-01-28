'''
Challenge : Code blocks and indentation
Level 1
The following code contains at least one indentation error. Find and fix the error(s) so the program prints the radius, area, and circumference of a circle.
'''
import math

# Fix the indentation in the code below
radius = int(input())
area = math.pi * radius * radius
circumference = 2 * math.pi * radius

print(f'Radius: {radius} ft')
print(f'Area: {area:.1f} ft^2')
print(f'Circumference: {circumference:.1f} ft')

'''
Level 2
The following code contains at least one indentation error. Find and fix the error(s) so the program works as follows:
    If var1 is less than or equal to var2, then 'var1 is less than or equal to var2' is output.
    Otherwise, 'var1 is greater than var2' is output.
'''
var1 = int(input())
var2 = int(input())

# Fix the indentation in the code below
if var1 <= var2:
    print('var1 is less than or equal to var2')
else:
    print('var1 is greater than var2')

'''
Level 3
The following program outputs the age category that corresponds to a value read from input, but the code does not follow the standard recommended four columns per indentation. Change the code to follow the standard indentation.
'''
num_oranges = int(input())
oranges_wanted = int(input())

# Fix the indentation in the code below
if num_oranges >= oranges_wanted:
    if num_oranges > oranges_wanted:
        print(f'{num_oranges - oranges_wanted} extra oranges')
    else:
        print('Enough oranges')
else:
    print('Not enough oranges')

'''
Level 4
The following code outputs a string using values read from input, but the program contains a line with more than 80 columns. Use implicit line joining to join the long string in animal_str so that the program does not contain any lines with more than 80 columns.
'''
adjective1 = input()
adjective2 = input()

# Modify the following line
animal_str = ("Sam's favorite exhibit to look at when she goes to the "
              "zoo is the raccoon exhibit. She thinks the raccoons are "
              "{0} and {1}.")

# format() replaces the curly braces in a string with variables.
# This method is being used to test your code.
new_str = animal_str.format(adjective1, adjective2)
print(new_str)