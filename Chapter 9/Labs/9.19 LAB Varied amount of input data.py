'''
Docstring for Chapter 9.Labs.9.19 Varied amount of input data
Statistics are often calculated with varying amounts of input data. Write a program that takes any number of non-negative floating-point numbers as input, and outputs the max and average, respectively.

Output the max and average with two digits after the decimal point.
Ex: If the input is:
14.25 25 0 5.75
the output is:
25.00 11.25
'''
user_input = list(map(float, input().split()))

max_val = max(user_input)
average = sum(user_input) / len(user_input)

print(f'{max_val:.2f} {average:.2f}')