'''
Challenge : List comprehensions
Level 1
List data_list contains integers read from input. Assign updated_list with a new list where each element is three times the corresponding element in data_list.

Click here for example
Ex: If the input is 19 16 7 1, then the output is:

Original: [19, 16, 7, 1]
Updated: [57, 48, 21, 3]
'''
data_list = []

# Read input
tokens = input().split()
for token in tokens:
    data_list.append(int(token))

updated_list = [number * 3 for number in data_list]

print(f'Original: {data_list}')
print(f'Updated: {updated_list}')

'''
Level 2
List input_list contains floats read from input. Use list comprehension to convert each float in input_list to a string showing the float to three decimal places. Then, assign calibrated_list with the new list returned by list comprehension.

Click here for example
Ex: If the input is 1.75 0.25 2.0 7.25, then the output is:
Floats: [1.75, 0.25, 2.0, 7.25]
As strings: ['1.750', '0.250', '2.000', '7.250']

Note: f'{x:.3f}' converts float x to a string showing x to three decimal places.
'''
input_list = []

# Read input
for token in input().split():
	input_list.append(float(token))

calibrated_list = [f"{i:.3f}" for i in input_list]

print(f'Floats: {input_list}')
print(f'As strings: {calibrated_list}')

'''
Level 3
List raw_list contains integers read from input. Assign accepted_list with the new list containing all the numbers that are greater than or equal to 29 in raw_list, in that order.

Click here for example
Ex: If the input is 42 19 42 4, then the output is:
All numbers: [42, 19, 42, 4]
Numbers greater than or equal to 29: [42, 42]
'''
# Read input
raw_list = [int(x) for x in input().split()]

accepted_list = [number for number in raw_list if number >= 29]

print(f'All numbers: {raw_list}')
print(f'Numbers greater than or equal to 29: {accepted_list}')

'''
Level 4
Integer num_rows is read from input, representing the number of rows in a two-dimensional list. List input_list is a two-dimensional list containing the remaining integers read from input. Assign computed_list with the new list containing the number of elements in each row of input_list.

Click here for example
Ex: If the input is:
3
27 24 20
15 45
20 32 42

then the output is:
All numbers: [[27, 24, 20], [15, 45], [20, 32, 42]]
Number of elements in each row: [3, 2, 3]
Note: len(a_list) returns the number of elements in a_list.
'''
# Read input
num_rows = int(input())
input_list = []
for i in range(num_rows):
    input_list.append([int(x) for x in input().split()])

computed_list = [len(number) for number in input_list]

print(f'All numbers: {input_list}')
print(f'Number of elements in each row: {computed_list}')

'''
Level 5
Integer num_rows is read from input, representing the number of rows in a two-dimensional list. List input_list is a two-dimensional list containing the remaining integers read from input. Assign computed_value with the sum of the row with the smallest sum in input_list.

Click here for example
Ex: If the input is:
3
48 31 16
35 10 3 12
27 5 36 13
then the output is:
All numbers: [[48, 31, 16], [35, 10, 3, 12], [27, 5, 36, 13]]
Sum of the row with the smallest sum: 60

Note:
    min(a_list) returns the smallest element in a_list given that a_list contains numbers only.
    sum(a_list) returns the sum of all the elements in a_list given that a_list contains numbers only.
'''
# Read input
num_rows = int(input())
input_list = []
for i in range(num_rows):
    input_list.append([int(x) for x in input().split()])

computed_value = min([sum(row) for row in input_list])

print(f'All numbers: {input_list}')
print(f'Sum of the row with the smallest sum: {computed_value}')