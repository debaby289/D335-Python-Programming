'''
Write a program that repeatedly reads in integers until a negative integer is read. The program also keeps track of the largest integer that has been read so far and outputs the largest integer at the end.

Ex: If the input is:
    2
    77
    17
    4
    -1

the output is:
    Largest integer: 77

Assume a user will enter at least one non-negative integer.
'''
num = int(input())
max_num = num

while num >= 0:
    num = int(input())

    if num > max_num:
        max_num = num

print(f'Largest integer: {max_num}')