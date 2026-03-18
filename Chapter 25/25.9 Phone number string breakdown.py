'''
Given a string representing a 10-digit phone number, output the area code, prefix, and line number using the format (800) 555-1212.

Ex: If the input is:
    8005551212
the output is:
    (800) 555-1212

Hint: Use string slicing operators.

For simplicity, assume all phone numbers are 10-digit. So 18005551212 is not allowed.
'''
phone_number = input()

area = phone_number[:3]
prefix = phone_number[3:6]
line = phone_number[6:]

print(f"({area}) {prefix}-{line}")