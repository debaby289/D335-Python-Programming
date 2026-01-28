'''
Docstring for Chapter 5.Challenges.5.12.2 Conditional expression Print negative or nonnegative
Create a conditional expression that evaluates to string "negative" if user_val is less than 0, and "nonnegative" otherwise.
'''
user_val = int(input())

cond_str = 'negative' if user_val < 0 else 'nonnegative'

print(f'{user_val} is {cond_str}')