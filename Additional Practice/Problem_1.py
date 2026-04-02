'''
PROBLEM 1: Temperature Converter Function
Write a function celsius_to_fahrenheit(celsius) that:

Takes a Celsius temperature as a parameter
Returns the Fahrenheit equivalent
Formula: F = (C × 9/5) + 32

Then write a main program that:

Asks the user for a temperature in Celsius
Calls the function
Prints the result to 1 decimal place

Expected output:
Enter temperature in Celsius: 25
25.0°C is 77.0°F
'''
#Function definition
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

if __name__ == '__main__':
    celsius = float(input('Enter temperature in Celsius: '))

    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f'{celsius}C is {fahrenheit}F')