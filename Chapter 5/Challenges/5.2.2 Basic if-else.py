'''
Challenge : Basic if-else
Level 1
Write an if-else statement for the following:

If barcode_check_digit is equal to 6, execute group_id = 1. Else, execute group_id = barcode_check_digit.
Ex: If barcode_check_digit is 3, then group_id = 3.
'''
barcode_check_digit = int(input())  # Program will be tested with values: 5, 6, 7, 8.

if barcode_check_digit == 6:
    group_id = 1
else:
    group_id = barcode_check_digit

print(group_id)


'''
Level 2
Write an if-else statement for the following:

If num_difference is equal to -16, execute total_difference = -25. Else, execute total_difference = num_difference.
'''
num_difference = int(input())  # Program will be tested with values: -14, -15, -16, -17.

if num_difference == -16:
    total_difference = -25
else:
    total_difference = num_difference

print(total_difference)

