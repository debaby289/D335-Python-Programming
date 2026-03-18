'''
Write a program that reads a list of integers, and outputs the two smallest integers in the list, in ascending order.

Ex: If the input is:
    10 5 3 21 2

the output is:
    2 and 3
Hint: Make sure to initialize the second smallest and smallest integers properly.
'''
nums = list(map(int, input().split()))

smallest = float('inf')
second_smallest = float('inf')

for num in nums:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest:
        second_smallest = num

print(f"{smallest} and {second_smallest}")