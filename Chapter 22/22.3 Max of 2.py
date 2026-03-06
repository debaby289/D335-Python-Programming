'''
Write a program that takes in two integers and outputs the larger value. If the two integers are the same, output the integers' value.

Ex: If the input is:
    4 
    2

the output is:
    Max of 4 and 2 is 4
'''
int_1 = int(input())
int_2 = int(input())

if int_1 == int_2:
    print(f'Max of {int_1} and {int_2} is {int_1}')
elif int_1 > int_2:
    print(f'Max of {int_1} and {int_2} is {int_1}')
else:
    print(f'Max of {int_1} and {int_2} is {int_2}')