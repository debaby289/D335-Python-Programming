'''
Write a program that reads a list of integers into a list as long as the integers are greater than zero, then outputs the smallest and largest integers in the list.

Ex: If the input is:
    10
    5
    3
    21
    2
    -6

the output is:
    2 and 21

You can assume that the list of integers will have at least 2 values
'''
numbers = []
num = int(input())  # Read first number

while num > 0:  # Continue as long as greater than zero
    numbers.append(num)
    num = int(input())  # Read next number

smallest = min(numbers)
largest = max(numbers)
print(f'{smallest} and {largest}')