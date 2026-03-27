'''
Task:
Create a solution that accepts an integer input representing a 9-digit unformatted student identification number. Output the identification number as a string with no spaces.

The solution output should be in the format:
    xxx-xx-xxxx

Sample Input and Output:
If the input is
Enter Student Identification Number:
    123456789
then the expected output is
    123-45-6789

NOTE: you do not need to write any logic into your program to handle input exceptions (e.g., integers with greater than or less than 9 digits)
'''
#solution accepts a 9-digit integer representing an unformatted student identification number (e.g.,"5417543010")
#solution outputs formatted student identification number as a string (e.g.,"541-75-3010")
#accept integer input
print("Enter Student Identification Number:")
identification_number = int(input())

three_digits = identification_number // 1000000
two_digits = (identification_number // 10000) % 100
four_digits = identification_number % 10000

print(f'{three_digits}-{two_digits}-{four_digits}')
