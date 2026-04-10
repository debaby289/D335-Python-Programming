'''
Write a program that:
    Asks for a 10-digit phone number (like 5551234567)
    Formats it as: (555) 123-4567
    Uses // and % to extract the parts

Hint:
    First 3 digits: number // 10000000
    Next 3 digits: (number // 10000) % 1000
    Last 4 digits: number % 10000

Expected output:
    Enter 10-digit phone number: 5551234567
    Formatted: (555) 123-4567
'''
phone_no = int(input('Enter 10-digit phone number: '))

area_code = phone_no // 10000000
three_digits = (phone_no // 10000) % 1000
four_digits =  phone_no % 10000

print(f'({area_code}) {three_digits}-{four_digits}')