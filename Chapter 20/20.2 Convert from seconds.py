'''
People find it easier to read time in seconds, minutes, and hours rather than just seconds.

Write a program that reads in seconds as input, and outputs the time in seconds, minutes, and hours.

Ex: If the input is:
    4000

the output is:
    Seconds: 40
    Minutes: 6
    Hours: 1
'''
total_seconds = int(input())

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = (total_seconds % 3600) % 60

print(f'Seconds: {seconds}')
print(f'Minutes: {minutes}')
print(f'Hours: {hours}')
