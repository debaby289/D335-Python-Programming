'''
Given a list of integers, output those integers separated by a comma and space, except for the last which should be followed by a period (and newline). The first integer indicates how many integers are in the subsequent list.

Ex: If the input is:
    4 
    1 
    7 
    3 
    5 

The output should be:
    1, 7, 3, 5.

Hints:
    Read in the first integer as num_ints, followed by a for loop that loops num_ints times.

    Decide whether to print the comma and space AFTER printing the current integer, or BEFORE. For each possibility, figure out how you'll handle the special cases of the first and last items, and then decide whether after or before is the best approach.

    You can print the period and newline after the above for loop.

    Assume the first integer will always accurately show the number of integers following it. Ex. 3 1 7 3 5 will not be possible.
'''

num_ints = int(input())
numbers = []

for i in range(num_ints):
    numbers.append(int(input()))

for i in range(len(numbers)):
    if i < len(numbers) - 1:
        print(numbers[i], end=', ')
    else:
        print(numbers[i], end='.\n')