'''
Write a program that:
    Asks for two numbers
    Divides the first by the second
    Handles these exceptions:
        ValueError: If input is not a number
        ZeroDivisionError: If dividing by zero

Prints appropriate error messages or the result
'''
try:
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

    div = num1 / num2

    print(f'Result: {div}')

except ValueError:
    print('Error: Invalid input - please enter numbers')

except ZeroDivisionError:
    print('Error: Cannot divide by zero')