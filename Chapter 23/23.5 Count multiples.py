'''
Write a program that takes three integers as input: low, high, and x. The program then outputs the number of multiples of x between low and high exclusive.

Ex: If the input is:
    1
    10
    2
the output is:
    Multiples of 2: 2,4,6,8,

For coding simplicity, follow each output number by a comma, even the last one.

Hint: Use the % operator to determine if a number is a multiple of x. Use a for loop to test each number between low and high.
'''
low_num = int(input())
high_num = int(input())
x = int(input())

print(f'Multiples of {x}: ', end='')

for i in range(low_num + 1 ,high_num):
    if i % x == 0:
        print(i,end=',')

print()