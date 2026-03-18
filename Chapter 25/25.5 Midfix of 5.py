'''
The midfix of 5 is the middle five characters of a string. Given a string input, output the middle five characters of that string with a new line at the end. Assume the string length is always odd and at least five characters.

Ex: If the input is:
    xxxplanexxx
the output is:
    Midfix: plane
'''
user_input = input()

mid = len(user_input) // 2
midfix = user_input[mid - 2 : mid + 3]

print(f"Midfix: {midfix}")