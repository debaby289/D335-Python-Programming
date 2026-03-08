'''
Write a program that takes in three lowercase characters and outputs the characters in alphabetical order.

Hint: Ordering three characters takes six permutations.

Ex: If the input is:
    c
    a
    b
the output is:
    a b c
'''
alp = []

for i in range(3):
    char = input()
    alp.append(char)

alp = sorted(alp)
print(' '.join(alp))