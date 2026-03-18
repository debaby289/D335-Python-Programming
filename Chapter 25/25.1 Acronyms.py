'''
An acronym is a word formed from the initial letters of words in a set phrase. Write a program whose input is a phrase and whose output is an acronym of the input. Append a period (.) after each letter in the acronym. If a word begins with a lower case letter, don't include that letter in the acronym. Assume the input has at least one upper case letter.

Ex: If the input is:
    Institute of Electrical and Electronics Engineers
the output is:
    I.E.E.E.

Ex: If the input is:
    Association for computing MACHINERY
the output is:
A.M.

Although the letters ACHINERY in MACHINERY are upper case, those letters are omitted for being a part of the word MACHINERY.

Hint: Use isupper() to check if a letter is upper case.
'''
phrase = input()
finals = []

char_list = phrase.split()

for char in char_list:
    if char[0].isupper():
        finals.append(char[0])

caps = '.'.join(finals)
print(f'{caps}.')

