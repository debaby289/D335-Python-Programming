'''
Docstring for Chapter 7.7.1.2 Basic function call
Complete the function definition to return the hours given minutes.

Sample output with input: 210.0
3.5
'''

def get_minutes_as_hours(orig_minutes):
    hours = orig_minutes / 60
    return hours

minutes = float(input())
print(get_minutes_as_hours(minutes))