'''
When analyzing data sets, such as data for human heights or for human weights, a common step is to adjust the data. This can be done by normalizing to values between 0 and 1, or throwing away outliers. For this program, adjust the values by subtracting each value from the maximum. Input values should be added to the list until -1 is entered.

Ex: If the input is:    
    30
    50
    10
    70
    65
    -1

the output is:
    40
    20
    60
    0
    5

Your program must define and call the function:
def get_max_int(nums)

Note: get_max_int() returns the maximum value in the list.
'''
def get_max_int(nums):
    max_val = nums[0]
    
    for num in nums:
        if num > max_val:
            max_val = num
            
    return max_val


if __name__ == '__main__':
    nums = []
    
    while True:
        val = int(input())
        if val == -1:
            break
        nums.append(val)
    
    max_val = get_max_int(nums)
    
    for num in nums:
        print(max_val - num)