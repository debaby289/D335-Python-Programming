'''
Docstring for Chapter 8.Labs.8.10 LAB Mad Lib - loops
Write a program that takes a string and an integer as input, and outputs a sentence using the input values as shown in the example below. The program repeats until the input string is quit and disregards the integer input that follows.

Ex: If the input is:
apples 5
shoes 2
quit 0

the output is:
Eating 5 apples a day keeps you happy and healthy.
Eating 2 shoes a day keeps you happy and healthy.
'''
user_input = input()

while not user_input.startswith('quit'):
    item,count = user_input.split(' ')
    print(f'Eating {count} {item} a day keeps you happy and healthy.')
    user_input = input()