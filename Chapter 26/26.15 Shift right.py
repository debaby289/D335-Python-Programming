'''
Write a program that reads a list of integers from input and modifies the list by shifting each element to the right one position and by shifting the last element to the first position. The input begins with an integer indicating the number of values that follow. Output the modified list and end with a newline.

Ex: If the input is:
    6 
    2
    4
    6
    8
    10
    12

the output is:
    12 2 4 6 8 10 
For coding simplicity, follow every output value by a space, including the last one.
'''
user_values = []

n = int(input())

for _ in range(n):
    user_values.append(int(input()))

# Rotate right by 1
last = user_values[-1]

for i in range(n - 1, 0, -1):
    user_values[i] = user_values[i - 1]

user_values[0] = last

# Output
for num in user_values:
    print(num, end=" ")

print()