'''
Challenge : Ranges with gaps
Level 1
Integer num_carrots is read from input representing the number of carrots. Output 'Unfitting amount' if:
    the number of carrots is fewer than 5.
    or the number of carrots is more than 10.
'''
num_carrots = int(input())

if (num_carrots < 5) or (num_carrots > 10):
    print('Unfitting amount')

'''
Level 2
Float temperature_in_celsius is read from input representing a temperature in degrees Celsius. If the temperature is colder than 15.5 degrees Celsius or warmer than 80.5 degrees Celsius, output 'Skip'. Otherwise, output 'Admit'.
'''
temperature_in_celsius = float(input())

if (temperature_in_celsius < 15.5) or (temperature_in_celsius > 80.5):
    print('Skip')
else:
    print('Admit')

'''
Level 3
Integer ordered_cups is read from input representing the number of cups. Output:
    'Medium box', if there are 40 - 80 cups inclusive.
    'Large box', if there are 130 - 140 cups inclusive.
'''
ordered_cups = int(input())

if (ordered_cups >= 40) and (ordered_cups <= 80):
    print('Medium box')
elif (ordered_cups >= 130) and (ordered_cups <= 140):
    print('Large box')

'''
Level 4
Integer supplied_cups is read from input representing the number of cups. Output:
    'Basic container', if the number of cups is greater than or equal to 25 and less than or equal to 35.
    'Standard container', if the number of cups is greater than or equal to 70 and less than 95.
    'Select another amount', otherwise.
'''
supplied_cups = int(input())

if (supplied_cups >= 25) and (supplied_cups <= 35):
    print('Basic container')
elif (supplied_cups >= 70) and (supplied_cups < 95):
    print('Standard container')
else:
    print('Select another amount')