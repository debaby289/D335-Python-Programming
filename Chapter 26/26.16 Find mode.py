'''
Write a program that reads a sequence of integers from input and identifies the mode (the value that appears most often). The input is a sequence of integers that ends with -1. All other integers in the sequence are between 1 and 20 (inclusive). Total number of integers in the sequence is unknown. Output the mode and end with a newline. Assume that the sequence is not empty and only one mode exists.

Hint: Use a list to count the number of occurrences of 1-20. See comment in starter code.

Ex: If the input is:
    5
    9
    2
    2
    1
    4
    5
    5
    -1

the output is:
    5
'''
# num_count [] counts the number of occurrences for values 1-20
# index 0 is ignored
num_count = [0] * 21

# Read input and count occurrences
while True:
    num = int(input())
    if num == -1:
        break
    num_count[num] += 1

# Find the mode
max_count = 0
mode = 0

for i in range(1, 21):
    if num_count[i] > max_count:
        max_count = num_count[i]
        mode = i

print(mode)