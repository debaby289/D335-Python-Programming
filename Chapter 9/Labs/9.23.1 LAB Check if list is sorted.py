'''
Docstring for Chapter 9.Labs.9.23.1 LAB Check if list is sorted
Write the in_order() function, which has a list of integers as a parameter, and returns True if the integers are sorted in descending order (in order from high to low) or False otherwise. The program outputs "In descending order" if the list is sorted, or "Not in order" if the list is not sorted.

Ex: If the list passed to the in_order() function is [5, 6, 7, 8, 3], then the function returns False and the program outputs:
Not in order

Ex: If the list passed to the in_order() function is [10, 8, 7, 6, 5], then the function returns True and the program outputs:
In descending order
Note: Use a for loop. DO NOT use sorted() or sort().
'''
'''
write in_order function with last as a parameter
return true if the list is sorted from hight to low -- print(f'In descending order')
return false if the list is sorted from low to high -- print(f'Not in order')
'''

#starter code
def in_order(nums):
    for i in range(len(nums) - 1):
        if nums[i] < nums[i+1]:
            return False
        
    return True
    
if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In descending order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [10, 8, 7, 6, 5]
    if in_order(nums2):
        print('In descending order')
    else:
        print('Not in order')
