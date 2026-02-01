'''
Docstring for Chapter 6.Labs.6.16.1: LAB: Adjust values in a list by normalizing

Instructor note:
Hint: Two for loops will be needed for this lab, one to get the input data and then one to process.

When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. This adjustment can be done by normalizing to values between 0 and 1, or throwing away outliers.
For this program, adjust the values by dividing all values by the largest value. The input begins with an integer indicating the number of floating-point values that follow. Assume that the list will always contain positive floating-point values.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input is:
5
30.0
50.0
10.0
100.0
65.0

the output is:
0.30
0.50
0.10
1.00
0.65

The 5 indicates that there are five floating-point values in the list, namely 30.0, 50.0, 10.0, 100.0, and 65.0. 100.0 is the largest value in the list, so each value is divided by 100.0.
'''
#Get number of values
num_values = int(input())

#Store values in an emty list
values = []

#store max
max_value = 0

#Loop through the num_values
for value in range(num_values):
    values.append(float(input()))  #The inputs are stord as floats

#Find the max
for nums in values:
    if nums > max_value:
        max_value = nums

#Max range division 
for i in range(num_values):
    values[i] = values[i] / max_value
    print(f'{values[i]:.2f}')