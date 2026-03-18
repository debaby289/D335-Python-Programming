'''
The prefix of 5 is the first five characters of a string. Given a string input, output the first five characters of that string. Assume the string will always have at least five characters.

Ex: If the input is:
    fantastic
the output is:
    Prefix: fanta
'''
user_input = input()

prefix = user_input[:5]

print(f"Prefix: {prefix}")