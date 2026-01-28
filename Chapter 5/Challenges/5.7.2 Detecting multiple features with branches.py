'''
Challenge : Detecting multiple features with branches
Level 1
car_date is read from input. Write multiple if statements:
    If car_date is after 1933, then output 'Probably has a radio.'
    If car_date is before 1964, then output 'Probably only has a few safety features.'
    If car_date is after 1980, then output 'Probably has seat belts.'
'''
car_date = int(input())

if car_date > 1933:
    print('Probably has a radio.')

if car_date < 1964:
    print('Probably only has a few safety features.')

if car_date > 1980:
    print('Probably has seat belts.')

'''
Level 2
num_points1 and num_points2 are read from input. Write one if statement and one if-else statement:

If num_points1 is less than or equal to 25, then output 'num_points1 is less than or equal to 25.'
If num_points2 is greater than or equal to 40, then assign num_points2 with 6.
Otherwise, output 'num_points2 is less than 40.'
'''
num_points1 = int(input())
num_points2 = int(input())

if num_points1 <= 25:
    print('num_points1 is less than or equal to 25.')

if num_points2 >= 40:
    num_points2 = 6
else:
    print('num_points2 is less than 40.')

print(f'num_points2 is {num_points2}.')

'''
Level 3
Integers num_melons and cash_in_hand are read from input. Each melon costs 4 dollars.

Write the following if-else statement. Within the else branch, write the following assignment and nested if-else statement:
    If num_melons is less than 6, output 'Must purchase at least 6 melons'.
    Otherwise:
        Assign variable total_cost with the product of num_melons and 4.
        If total_cost is less than or equal to cash_in_hand, then output 'Approved transaction'.
        Otherwise, output 'Not enough money to buy all'.
'''
num_melons = int(input())
cash_in_hand = int(input())

if num_melons < 6:
    print('Must purchase at least 6 melons')
else:
    total_cost = num_melons * 4
    if total_cost <= cash_in_hand:
        print('Approved transaction')
    else:
        print('Not enough money to buy all')

