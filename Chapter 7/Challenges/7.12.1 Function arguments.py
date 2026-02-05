'''
Challenge : Function arguments
Level 1
values_list and number are read from input. multiply_nums() has two parameters list_to_modify and num, and multiplies each element of list_to_modify by num. Call multiply_nums() with a copy of the list values_list and number as the arguments to avoid modifying values_list.

Click here for example
Ex: If the input is:
2 10 3 6 5 8 1 4 9
90

then the output is:
Modified list: [180, 900, 270, 540, 450, 720, 90, 360, 810]
Original list: [2, 10, 3, 6, 5, 8, 1, 4, 9]

'''
def multiply_nums(list_to_modify, num):
    for i, element in enumerate(list_to_modify):
        list_to_modify[i] = element * num
    print(f'Modified list: {list_to_modify}')

values_list = [int(x) for x in input().split()]
number = int(input())

multiply_nums(list(values_list), number)

print(f'Original list: {values_list}')

'''
Level 2
Write a function add_one_element() that appends the element 'end' one time to the end of a list parameter.

Click here for example
Ex: If the input is:
I love you, you love me, we're a happy family

then the output is:
['I', 'love', 'you,', 'you', 'love', 'me,', "we're", 'a', 'happy', 'family', 'end']
'''
def add_one_element(list):
    list.append('end')

val_list = input().split()

add_one_element(val_list)
print(val_list)
