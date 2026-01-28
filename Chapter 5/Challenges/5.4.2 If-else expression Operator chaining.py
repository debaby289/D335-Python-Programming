'''
Docstring for Chapter 5.Challenges.5.4.2 If-else expression Operator chaining

Variable user_grade is read from input. Use operator chaining to complete the if-else expression as follows:
    If the value of user_grade is between 9 and 12 (both inclusive), then 'in high school' is output.
    Otherwise, 'not in high school' is output.

Ex 1: If the input is 10, then the output is:
in high school
Ex 2: If the input is 8, then the output is:
not in high school

Note: 0 < x < 5 evaluates to true if x is between the ranges 0 and 5 (both non-inclusive).
'''
user_grade = int(input())

if 9 <= user_grade  <=12 :
    print('in high school')
else:
    print('not in high school')