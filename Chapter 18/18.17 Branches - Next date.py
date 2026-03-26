'''
Many websites let users make reservations (hotel, car, flights, etc.). When a user selects a date, the next day is often automatically selected (for hotel checkout, car return, flight return, etc.). Given a date in the form of three integers, output the next date.

Ex: If the input is
    1 
    15 
    2017
The output should be
    1 16 2017

Ex: If the input is
    8 
    31 
    2017
The output should be
    9 1 2017

Ignore leap years.

Hints:
    Group the months based on number of days. Then create an if-else statement for each case.
    Note that 12 (December) is a special case; after the last day, the next month is 1 (January) and is the next year.
'''
month = int(input())
date = int(input())
year = int(input())

if month == 2 and date == 28:
    month += 1
    date = 1
elif month in [4,6,9,11] and date == 30:
    month += 1
    date = 1
elif date == 31:
    if month == 12:
        month = 1
        year += 1
        date = 1
    else:
        month += 1
        date = 1
else:
    date += 1

print(f'{month} {date} {year}')