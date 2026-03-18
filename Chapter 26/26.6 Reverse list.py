'''
Complete the reverse_list() function that returns a new integer list containing all contents in the list parameter but in reverse order.

Ex: If the elements of the input list are:
    [2, 4, 6]

the returned array will be:
    [6, 4, 2]
Note: Use a for loop. DO NOT use reverse() or reversed().
'''
def reverse_list(li):
    reversed_list = []

    for i in range(len(li) - 1, -1, -1):
        reversed_list.append(li[i])

    return reversed_list
    
    
if __name__ == '__main__':
    int_list = [2, 4, 6]
    print(reverse_list(int_list)) 