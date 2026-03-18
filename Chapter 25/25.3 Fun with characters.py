'''
Complete the check_character() function which has 2 parameters: A string and a specified index. The function checks the character at the specified index of the string parameter, and returns a string based on the type of character at that location indicating if the character is a letter, digit, whitespace, or unknown character.

Ex: The function calls below with the given arguments will return the following strings:
    check_character('happy birthday', 2) returns "Letter: 'p'"
    check_character('happy birthday', 5) returns "Whitespace: ' '"
    check_character('happy birthday 2 you', 15) returns "Digit: '2'"
    check_character('happy birthday!', 14) returns "Unknown: '!'"
'''

def check_character(word, index):
    char = word[index]

    if char.isalpha():
        return f"Letter: '{char}'"
    elif char.isdigit():
        return f"Digit: '{char}'"
    elif char.isspace():
        return f"Whitespace: '{char}'"
    else:
        return f"Unknown: '{char}'"
  
if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))

