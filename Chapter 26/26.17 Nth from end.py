'''
Write a program that reads a list of positive integers followed by a negative integer from input and outputs the Nth number from the end of the list. Convert the negative integer read at the end to positive and use as N. Output the negative integer read at the end if the size of the list is smaller than N.

Ex: If the input is:
    1 5 9 7 5
    -3
the output is:
    9

Ex: If the input is:
    1 2 3 4 5
    -6
the output is:
    -6
'''
nums = list(map(int, input().split()))
n = int(input())

N = abs(n)

if len(nums) < N:
    print(n)
else:
    print(nums[-N])