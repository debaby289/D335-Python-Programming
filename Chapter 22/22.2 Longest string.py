'''
Write a program that takes two strings and outputs the longer string, followed by "is longer than", and the shorter string. If the strings have the same length then output the strings followed by "are the same length".

Ex. If the input is:
    almond
    pistachio

the output is:
    pistachio is longer than almond
'''
string_1 = input()
string_2 = input()

if len(string_1) == len(string_2):
    print(f'{string_1} and {string_2} are the same length')
elif len(string_1) > len(string_2):
    print(f'{string_1} is longer than {string_2}')
else: 
    print(f'{string_2} is longer than {string_1}')