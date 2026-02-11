'''
Docstring for Chapter 8.Labs.8.11 LAB Remove all non-alpha characters
Write a program that removes all non-alpha characters from the given input.

Ex: If the input is:
-Hello, 1 world$!
the output is:
Helloworld
'''
user_input = input()

string = ''

for user in user_input:
    if user.isalpha():
        string += user

print(string)
