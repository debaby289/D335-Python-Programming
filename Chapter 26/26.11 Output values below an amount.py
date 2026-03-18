'''
Write a program that first gets a list of integers from input. The last value of the input represents a threshold. Output all integers less than or equal to that threshold value. Do not include the threshold value in the output.

For simplicity, follow each number output by a comma, including the last one.

Ex: If the input is:
    50 60 140 200 75 100
the output is:
    50,60,75,

Such functionality is common on sites like Amazon, where a user can filter results.
'''
nums = list(map(int, input().split()))

threshold = nums[-1]
values = nums[:-1]

for num in values:
    if num <= threshold:
        print(num, end=",")