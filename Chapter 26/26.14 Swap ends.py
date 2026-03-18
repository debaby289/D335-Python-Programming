'''
Write a program that reads a list of integers from input and outputs the list with the first and last numbers swapped.

Ex: If the input is:
    1 2 3 4 5 6 7 8

the output is:
    8 2 3 4 5 6 7 1

For coding simplicity, follow every output value by a space, including the last one. The output ends with a newline.
'''
user_values = list(map(int, input().split()))

# Swap first and last elements
user_values[0], user_values[-1] = user_values[-1], user_values[0]

# Print with space after each number
for num in user_values:
    print(num, end=" ")
    
print()