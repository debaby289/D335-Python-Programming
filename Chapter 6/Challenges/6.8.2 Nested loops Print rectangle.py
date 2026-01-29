'''
Docstring for Chapter 6.Challenges.6.8.2 Nested loops Print rectangle

Given num_rows and num_cols representing the number of rows and columns, write nested loops using range() to print a rectangle as shown in the example below.

Ex: If the input is 2 3, then the output is:
* * * 
* * * 
Note: The inner loop should be indented once to contain the inner print statement.
'''
num_rows = int(input())
num_cols = int(input())

for i in range(num_rows):
    for j in range(num_cols):
        print('*', end=' ')
    print()