'''
Given a length of a list, followed by the list of unique numbers, write a program that outputs "Sorted" if the numbers are in ascending order, "Unsorted" otherwise.

Ex: If the input is
    5  
    1 
    3 
    6 
    7 
    9
The output is "Sorted".

Ex: If the input is
    3  
    10 
    8 
    2
The output is "Unsorted".

A list of size 0 or 1 is sorted.

Hints:
    Remember that only one violation makes the entire list unsorted.

    For simplicity, you don't have to don't break out of the loop if you find two numbers aren't ascending. Instead, use a bool variable, initialize it to true, and set it to false if you find any violation.
'''
num_list_size = int(input())
numbers = []
sorted_values = True

for num in range(num_list_size):
    numbers.append(int(input()))
    if num > 0:  
        if numbers[num - 1] > numbers[num]:
            sorted_values = False
        if numbers[num - 1] == numbers[num]:
            sorted_values = False

if sorted_values == True:
    print('Sorted')
else:
    print('Unsorted')
