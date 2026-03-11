'''
Write a program that reads a list of integers, one per line, until an * is read, then outputs those integers in reverse. For simplicity in coding output, follow each integer, including the last one, by a comma.

Note: Use a while loop to output the integers. DO NOT use reverse() or reversed().

Ex: If the input is:
    2
    4
    6
    8
    10
    *

the output is:
    10,8,6,4,2,
'''
num_list = []
while True:
    num = input()
    if num == '*':
        break
    num_list.append(int(num))

# Print in reverse using while loop
index = len(num_list) - 1
while index >= 0:
    print(num_list[index], end=',')
    index -= 1

print()