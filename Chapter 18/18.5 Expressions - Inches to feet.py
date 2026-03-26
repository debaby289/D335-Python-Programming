'''
Docstring for Chapter 18.Easy.18.5 Expressions - Inches to feet
Given a total amount of inches, convert the input into a readable output in feet and inches.

Ex: If the input is:
55

the output should be:
4'7"
'''
inches = int(input())

print(f'{inches // 12}\'{inches % 12}"')