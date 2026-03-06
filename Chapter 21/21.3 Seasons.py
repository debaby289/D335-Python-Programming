'''
Write a program that takes a date as input and outputs the date's season in the northern hemisphere. The input is a string to represent the month and an int to represent the day.

Ex: If the input is:
    April
    11

the output is:
    Spring

In addition, check if the string and int are valid (an actual month and day).

Ex: If the input is:
    Blue
    65

the output is:
    Invalid 

The dates for each season in the northern hemisphere are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19
'''
month = input()
day = int(input())

valid_months = ['January','February','March','April','May','June',
                'July','August','September','October','November','December']

# Check if month is valid
if month not in valid_months:
    print('Invalid')
# Check if day is valid
elif (month in ('January','March','May','July','August','October','December') and (day <= 0 or day > 31)) or \
     (month in ('April','June','September','November') and (day <= 0 or day > 30)) or \
     (month == 'February' and (day <= 0 or day > 28)):
    print('Invalid')
# If we get here, month and day are valid - determine season
else:
    if month in ('January','February'):
        print('Winter')
    elif month == 'March':
        if day <= 19:
            print('Winter')
        else:
            print('Spring')
    elif month in ('April','May'):
        print('Spring')
    elif month == 'June':
        if day <= 20:
            print('Spring')
        else:
            print('Summer')
    elif month in ('July','August'):
        print('Summer')
    elif month == 'September':
        if day <= 21:
            print('Summer')
        else:
            print('Autumn')
    elif month in ('October','November'):  # Fixed: was ==
        print('Autumn')
    elif month == 'December':
        if day <= 20:
            print('Autumn')
        else:
            print('Winter')