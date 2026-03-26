'''
Write a program that outputs the biggest difference (absolute value) between any successive pair of numbers in a list. Such a list might represent daily stock market prices or daily temperatures, so the difference represents the biggest single-day change. The input is the list size, followed by the numbers.

Ex: If the input is
    5 
    60 
    63 
    68 
    61 
    59

The output is
    7

Hints:
    Declare a variable for the current number, and another for the previous number. At the start of each loop iteration, set prev_num = curr_num, then get the next number into curr_num.

    Maintain a max difference variable. Initialize it with 0. In each loop iteration, check if the difference between curr_num and prev_num exceeds max_diff; if so, update max_diff with that difference.

    Don't forget to take the absolute value of the difference before the above comparison.

    Don't try to check the max difference for the first number in the list, since no previous number exists.

    Assume the list size will always be accurate. Ex. 4 60 63 68 61 59 will not be possible.
'''
import math

#Grab numbers size
numbers_size = int(input())

#Empty numbers
numbers = []

# Retrieve numbers values
for i in range(numbers_size):
    numbers.append(int(input()))

#Initial
max_diff = 0

#Check numbers values
for i in range(1,len(numbers)):
    prev_num = numbers[i-1]
    curr_num = numbers[i]

    diff_temp = abs(prev_num - curr_num)

    if diff_temp > max_diff:
        max_diff = diff_temp
    
print(max_diff)