'''
Challenge : Functions with branches/loops
Level 1
Define a function find_employee_tax() that takes one parameter as a person's age, and returns the person's tax percent. The tax percent is returned as follows:

If the person's age is 20 or less years old, then the tax percent is 0.3.
If the person's age is more than 20 and less than 40 years old, then the tax percent is 0.27.
Otherwise, the tax percent is 0.07.

Click here for examples
Ex 1: If the input is 15, then the output is:
Testing 48: 0.07
Testing user input: 0.3

Ex 2: If the input is 35, then the output is:
Testing 48: 0.07
Testing user input: 0.27

Ex 3: If the input is 45, then the output is:
Testing 48: 0.07
Testing user input: 0.07
'''
def find_employee_tax(age):
    if age <= 20:
        tax = 0.3
    elif (age > 20) and (age < 40):
        tax = 0.27
    else:
        tax = 0.07
    return tax

input_user_age = int(input())

print(f'Testing 48: {find_employee_tax(48)}')
print(f'Testing user input: {find_employee_tax(input_user_age)}')

'''
Level 2
Define a function output_values() that takes two parameters and outputs all integers starting with the first parameter and ending with the second on one line separated and ending with a space. The function does not return any value.

Click here for example
Ex: If the input is:
1
3

then the output is:

Testing static input: 
4 5 6 
Testing user input: 
1 2 3 

Note: Assume the first parameter is less than the second.
'''
def output_values(small,big):
    for i in range(small,big + 1):
        print(i, end=' ')

num1 = int(input())
num2 = int(input())

print('Testing static input: ')
output_values(4, 6)
print(f'\nTesting user input: ')
output_values(num1, num2)

