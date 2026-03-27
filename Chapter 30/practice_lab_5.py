'''
Task:
Create a solution that accepts five integer inputs. Output the sum of the five inputs three times, converting the inputs to the requested data type before finding the sum.
    First output: the sum of the five inputs as an integer value
    Second output: the sum of the five inputs after converting each input to a float value
    Third output: the concatenation of the five inputs after converting each input to a string

The solution output should be in the format:
    Integer: integer_sum_value
    Float: float_sum_value
    String: string_sum_value
'''
#solution accepts five integer inputs
#solution outputs three sums of input values; convert before calculating sum
#first output: the sum of the five inputs as an integer value
#second output: the sum of the five inputs after converting each input to a float value
#third output: the concatenation of the five inputs after converting each input to a string
#accept five integer inputs
print("Enter 1st number:")
num1 = int(input())
print("Enter 2nd number:")
num2 = int(input())
print("Enter 3rd number:")
num3 = int(input())
print("Enter 4th number:")
num4 = int(input())
print("Enter 5th number:")
num5 = int(input())

integers = num1 + num2 + num3 + num4 + num5
floats = float(num1 + num2 + num3 + num4 + num5)
strings = str(num1) + str(num2) + str(num3) + str(num4) + str(num5)

print(f'Integer: {integers}')
print(f'Float: {floats}')
print(f'String: {strings}')
