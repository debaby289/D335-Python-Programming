'''
Write a program that reads two lists of integers and outputs the sum of multiplying the corresponding list items.
Note: The size of the two lists must be the same.

Ex: If the input is:
    1 2 3
    3 2 1
the program calculates (1 * 3) + (2 * 2) + (3 * 1) and outputs
    10

Ex: If the input is:
    2 3 4 5
    1 1 1 1
the program calculates (2 * 1) + (3 * 1) + (4 * 1) + (5 * 1) and outputs
    14
'''
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

total = sum(a * b for a, b in zip(list1, list2))

print(total)