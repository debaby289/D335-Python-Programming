'''
Write a program that reads integers user_num and div_num as input, and output the integer quotient (user_num divided by div_num). Use a try block to perform all the statements. Use an except block to catch any ZeroDivisionError as a variable and output "Zero Division Exception: " followed by the exception message from the variable. Use another except block to catch any ValueError caused by invalid input as a variable and output "Input Exception: " followed by the exception message from the variable.

Note: ZeroDivisionError is raised when a division by zero happens. ValueError is raised when a user enters a value of different data type than what is defined in the program. Do not include code to raise any exception in the program.

Ex: If the input of the program is:
    15
    3
the output of the program is:
    5

Ex: If the input of the program is:
    10
    0
the output of the program is:
    Zero Division Exception: integer division or modulo by zero

Ex: If the input of the program is:
        15.5
        5
the output of the program is:
    Input Exception: invalid literal for int() with base 10: '15.5'
'''
try:
    user_num = int(input())
    div_num = int(input())

    total_num = user_num // div_num
    print(total_num)
    
except ZeroDivisionError as excpt:
    print(f'Zero Division Exception: {excpt}')

except ValueError as excpt:
    print(f'Input Exception: {excpt}')