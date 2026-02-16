'''
Challenge : Handling exceptions with math operations and common data types
Level 1
Complete the following tasks:
    Write an exception handler to catch ValueError and output 'math.sqrt(): Area cannot be negative.'
    Write an exception handler to catch ZeroDivisionError and output 'Rain per square meter = Rainfall / Area: Area cannot be zero.'

Click here to show example
Ex: If the input is -1.0, then the output is:
math.sqrt(): Area cannot be negative.

Ex: If the input is 0.0, then the output is:
Side of the square area: 0.0
Rain per square meter = Rainfall / Area: Area cannot be zero.
'''
import math

try:
	square_area = float(input())
	total_rainfall = 70.0
	print(f'Side of the square area: {math.sqrt(square_area)}')
	print(f'Rain per square meter: {total_rainfall / square_area}')

except ValueError:
    print(f'math.sqrt(): Area cannot be negative.')
except ZeroDivisionError:
    print(f'Rain per square meter = Rainfall / Area: Area cannot be zero.')

'''
Level 2
String food_word has value 'bread'. In the try block, integer string_index is read from input. The character at string_index of food_word is output. Complete the following tasks:
    Write an exception handler to catch ValueError and output 'int(): Input is not an integer.'
    Write an exception handler to catch IndexError and output 'String index is less than -5 or greater than 4.'

Click here to show example
Ex: If the input is eight, then the output is:
int(): Input is not an integer.

Ex: If the input is 15, then the output is:
String index is less than -5 or greater than 4.
'''
food_word = 'bread'

try:
	string_index = int(input())
	print(f"Character at index {string_index} is '{food_word[string_index]}'")

except ValueError:
    print(f'int(): Input is not an integer.')
except IndexError:
    print(f'String index is less than -5 or greater than 4.')
