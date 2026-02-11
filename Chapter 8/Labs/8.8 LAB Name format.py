'''
Docstring for Chapter 8.Labs.8.8 LAB Namee format
Many documents use a specific format for a person's name. Write a program that reads a person's name in the following format:

firstName middleName lastName (in one line) and outputs the person's name in the following format:

lastName, firstInitial.middleInitial.

Ex: If the input is:
Pat Silly Doe
the output is:
Doe, P.S.

If the input has the following format:
firstName lastName (in one line)
the output is:
lastName, firstInitial.

Ex: If the input is:
Julia Clark
the output is:
Clark, J.
'''
name = input()

temp_name = name.split()
if len(name.split()) == 3:
    print(f'{temp_name[2]}, {temp_name[0][0]}.{temp_name[1][0]}.')
else:
    print(f'{temp_name[1]}, {temp_name[0][0]}.')
    