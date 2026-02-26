'''
A state's Department of Motor Vehicles needs a program to generate license plate numbers. A license plate number consists of three letters followed by three digits, as in CBJ523. (So "number" is a bit inaccurate, but that's the standard word used for license plates). Assuming the plate numbers are given out in sequence, write a program that reads a current number as a string and outputs the next number.

Ex: If the input is
    CBJ523
the output should be:
    CBJ524

If the input is:
    CBJ999
the output should be:
    CBK000

For the last number "ZZZ999", the output of the next number is:
    AAA000

Steps:
    Save each character in the input string individually.
    Consider each of the six characters one at a time, starting from the right.
    If the character is less than the maximum value ('9' for digits, 'Z' for letters), increment the character by one. To increment a letter, use chr(ord(c) +1), where c contains the letter.
    If the character is at the maximum value, reset the character to '0' or 'A' respectively and set a boolean variable to true, indicating a "carry" is needed to increment the next character by one. (If a carry isn't needed, set to false).
    Repeat Steps 3 and 4 if a carry is needed.
    With the process mentioned above, 6 separate if-else statements are needed.
'''
plate_number = input()