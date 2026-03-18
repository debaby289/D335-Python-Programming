'''
When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. This adjustment can be done by normalizing to values between 0 and 1, or throwing away outliers.

For this program, read in a list of floats and adjust their values by dividing all values by the largest value. Output each value with two digits after the decimal point. Follow each number output by a space. Assume that the list will always contain positive floating-point values.

Ex: If the input is:
    30.0 50.0 10.0 100.0 65.0

the output is:
    0.30 0.50 0.10 1.00 0.65 
'''
nums = list(map(float, input().split()))

max_val = max(nums)

for num in nums:
    print(f"{num / max_val:.2f}", end=" ")

print()