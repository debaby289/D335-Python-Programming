'''
Docstring for Chapter 7.Labs.7.20 LAB Step counter

A pedometer treats walking 1 step as walking 2.5 feet. Define a function named feet_to_steps that takes a float as a parameter, representing the number of feet walked, and returns the number of steps walked as an integer by using int(). Then, write a main program that reads the number of feet walked as an input, calls function feet_to_steps() with the input as an argument, and outputs the number of steps returned from feet_to_steps().

Use floating-point arithmetic to perform the conversion.

Note: Converting a float to an integer may affect the result's accuracy.

Ex: If the input is:
150.5

the output is:
60

The program must define and call the following function:
def feet_to_steps(user_feet)
'''
# Define your function here 
def feet_to_steps(feet):
    user_feet = feet / 2.5
    return int(user_feet)


if __name__ == '__main__':
    # Type your code here.
    user_steps = float(input())

    print(f'{feet_to_steps(user_steps)}')