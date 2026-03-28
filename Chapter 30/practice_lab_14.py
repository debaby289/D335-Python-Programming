'''
Task:
Write a program that accepts two integer inputs from the user:
    A number for which the factorial will be calculated
    A number to compare the factorial result against
Use the built-in math module and its factorial() function to compute the factorial of the first input number. Then, compare the computed factorial to the second input number and display the following:
    The factorial value of the first input
    A Boolean value indicating whether the factorial is greater than the second input
The solution output should be in the format
    The factorial value of number is factorial_value
    Boolean_value

Sample Input and Output:
If the input is
    6
    500
then the expected output is
    The factorial value of 6 is 720
    True

Alternatively, if the input is
    4
    50
then the expected output is
    The factorial value of 4 is 24
    False
'''
#solution accepts integer input and integer comparison value
#solution outputs the factorial of the integer input 
#solution outputs Boolean identification of whether the factorial is greater than identified comparison value

#import math module and call factorial()
import math

#accepts integer input
print("Enter a number to calculate its factorial:")
factorial_num = int(input())
print("Enter a number to compare with the factorial:")
comparison_num = int(input())

#factorial method
result = math.factorial(factorial_num)

#greater than user_input_comparison?
comparison = result > comparison_num
#output factorial
print(f"The factorial value of {factorial_num} is {result}")

#output boolean
print(comparison)