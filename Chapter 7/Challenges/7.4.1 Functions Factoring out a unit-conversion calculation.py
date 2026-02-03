'''
Docstring for Chapter 7.Challenges.7.4.1 Functions Factoring out a unit-conversion calculation
Write a function so that the main program below can be replaced by the simpler code that calls function mph_and_minutes_to_miles(). Original main program:

Inputs:
miles_per_hour = float(input())
minutes_traveled = float(input())

Formulas:
hours_traveled = minutes_traveled / 60.0
miles_traveled = hours_traveled * miles_per_hour

Expected Output:
print(f'Miles: {miles_traveled:f}')


Sample output with inputs: 70.0 100.0
Miles: 116.666667
'''
def mph_and_minutes_to_miles(num1,num2):
    hours_traveled = num2 / 60.0
    miles_traveled = hours_traveled * num1
    return miles_traveled

miles_per_hour = float(input())
minutes_traveled = float(input())

print(f'Miles: {mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):f}')