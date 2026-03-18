'''
Write a program that removes all digits from the given input.

Ex: If the input is:
    1244Crescent

the output is:
    Crescent
The program must define and call the following function that takes a string as parameter and returns the string without any digits.

def remove_digits(user_string)
'''
def remove_digits(user_string):
    result = ""

    for char in user_string:
        if not char.isdigit():
            result += char

    return result


if __name__ == '__main__':
    user_input = input()
    print(remove_digits(user_input))