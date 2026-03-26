'''
Docstring for Chapter 18.Easy.18.8 Expressions-Phone numbers
Formatting makes text easier for the viewer to read. Given a 10-digit phone number, output the number in a format that is easier for a person to read.

Ex: If the input is:
1234567890

the output should be:
(123) 456-7890
'''
phonenumber = input()

print(f'({phonenumber[0:3]}) {phonenumber[3:6]}-{phonenumber[6:]}')
