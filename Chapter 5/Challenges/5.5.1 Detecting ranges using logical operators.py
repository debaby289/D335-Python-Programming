'''
Challenge : Detecting ranges using logical operators
Level 1
Modify the given if statement so that 'Mid-size town' is output if num_residents is in the range 950 - 4500 inclusive.
'''
num_residents = int(input())

# Modify the following line
if (num_residents >= 950) and (num_residents <= 4500):
    print('Mid-size town')
else:
    print('Not a mid-size town')

'''
Level 2
Large universities have enrollments in the range 9500 - 19500 inclusive. Write an if statement that outputs 'Not a large university' if the input size_input is not in this range. Otherwise, output 'Large university'.
'''
size_input = int(input())

if (size_input >= 9500) and (size_input <= 19500):
    print('Large university')
else:
    print('Not a large university')

'''
Level 3
The temperature of gold in degrees Celsius is read from input into variable temp_input. If temp_input is:
    < 1064 degrees Celsius, output 'The gold is now a solid.'
    ≥ 1064 degrees Celsius and ≤ 2701 degrees Celsius, output 'The gold is now a liquid.'

Otherwise, output 'The gold is now a gas.'
'''
temp_input = int(input())

if temp_input < 1064:
    print('The gold is now a solid.')
elif (temp_input >= 1064) and (temp_input <= 2701):
    print('The gold is now a liquid.')
else:
    print('The gold is now a gas.')

'''
Level 4
If zip_code is in the inclusive range:
    10000 - 29999, output 'Located in the Eastern US'.
    30000 - 79999, output 'Located in the Central US'.
    80000 - 99950, output 'Located in the Western US'.

Otherwise, output 'Invalid input'.
'''
zip_code = int(input())

if (zip_code >= 10000) and (zip_code <= 29999):
    print('Located in the Eastern US')
elif (zip_code >= 30000) and (zip_code <= 79999):
    print('Located in the Central US')
elif (zip_code >= 80000) and (zip_code <= 99950):
    print('Located in the Western US')
else:
    print('Invalid input')