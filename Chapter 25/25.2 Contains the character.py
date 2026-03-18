'''
Write a program that reads a character, then reads in a list of words. The output of the program is every word in the list that contains the character at least once. Assume at least one word in the list will contain the given character.

Ex: If the input is:
    z
    hello zoo sleep drizzle

the output is:
    zoo,drizzle,

Keep in mind that the character 'a' is not equal to the character 'A'.

For coding simplicity, follow each output word by a comma, even the last one. Do not end with newline.
'''
search = input()
phrase = input()

words = phrase.split()

for word in words:
    if search in word:
        print(word, end=",")
    