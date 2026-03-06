'''
Write a program that takes in three integers and outputs the median value (not the largest or smallest value).

Ex: If the input is:
    7
    1
    4

the output is:
    4
'''
numbers  = []

int_1 = int(input())
numbers .append(int_1)

int_2 = int(input())
numbers .append(int_2)

int_3 = int(input())
numbers .append(int_3)

value_list = sorted(numbers)
median = len(numbers ) // 2

print(f'{value_list[median]}')