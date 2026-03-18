'''
The postfix of 5 is the last five characters of a string. Given a string input, output the last five characters of that string. Assume the string will always have at least five characters.

Ex: If the input is:
    chicken
the output is:
    Postfix: icken
'''
user_input = input()

postfix = user_input[-5:]

print(f"Postfix: {postfix}")