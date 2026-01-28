'''
Docstring for Chapter 5.Labs.5.16 LAB Interstate highway numbers
Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90. Note: 200 is not a valid auxiliary highway because 00 is not a valid primary highway number.

Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west.

Ex: If the input is:
90

the output is:
I-90 is primary, going east/west.

Ex: If the input is:
290

the output is:
I-290 is auxiliary, serving I-90, going east/west.
'''
highway_number = int(input())

primary = 'Holding'
direction = 'north/south'

if 1 <= highway_number <= 99:
    if highway_number % 2 != 0:
        direction = 'north/south'
        print(f'I-{highway_number} is primary, going {direction}.')
    else:
        direction = 'east/west'
        print(f'I-{highway_number} is primary, going {direction}.')
elif 100 <= highway_number <= 999:
    primary = highway_number % 100
    if primary == 00:
        print(f'{highway_number} is not a valid interstate highway number.')
    else:
        if primary % 2 != 0:
            direction = 'north/south'
            print(f'I-{highway_number} is auxiliary, serving I-{primary}, going {direction}.')
        else:
            direction = 'east/west'
            print(f'I-{highway_number} is auxiliary, serving I-{primary}, going {direction}.')
else:
    print(f'{highway_number} is not a valid interstate highway number.')