'''
Write a program that reads in seconds, minutes, and hours as input, and outputs the time in seconds only.

Ex: If the input is:
    40
    6
    1

where 40 is the number of seconds, 6 is the number of minutes, and 1 is the number of hours, the output is:
    4000 seconds
'''
seconds = int(input())
minutes = int(input())
hours = int(input())

total_seconds = seconds + (minutes * 60) + (hours * pow(60,2))
print(f'{total_seconds} seconds')