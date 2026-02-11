'''
Challenge : 
Level 1
List raw_list contains integers read from input, representing data samples from an experiment. For each element in raw_list:
    If the element's value is less than 55, then output the element's value, followed by ' at index ', the element's index, and ' is rejected'.
    Otherwise, increment accepted_samples and output the element's value, followed by ' at index ', the element's index, and ' is accepted'.

Click here for example
Ex: If the input is 55 56 51 54, then the output is:
Raw samples: [55, 56, 51, 54]
55 at index 0 is accepted
56 at index 1 is accepted
51 at index 2 is rejected
54 at index 3 is rejected
Total accepted samples: 2
'''
# Read input and split input into tokens
# Read input and split input into tokens
tokens = input().split()

raw_list = []
for token in tokens:
    raw_list.append(int(token))

print(f'Raw samples: {raw_list}')

accepted_samples = 0

for raw in raw_list:
    if raw < 55:
        print(f'{raw} at index {raw_list.index(raw)} is rejected')
    else:
        print(f'{raw} at index {raw_list.index(raw)} is accepted')
        accepted_samples += 1

print(f'Total accepted samples: {accepted_samples}')

'''
Level 2
List pressure_data contains integers read from input, representing data samples from an experiment. Initialize variable sum_picked with 0. Then, for each element in pressure_data that is both at an odd-numbered index and less than 65:
    Output 'Index ', followed by the element's index, ': value is ', and the element's value.
    Increase sum_picked by each such element's value.

Click here for example
Ex: If the input is 64 51 57 66 86 65, then the output is:
All data: [64, 51, 57, 66, 86, 65]
Index 1: value is 51
Sum of selected elements is: 51
'''
# Read input and split input into tokens
# Read input and split input into tokens
tokens = input().split()

pressure_data = []
for token in tokens:
    pressure_data.append(int(token))

print(f'All data: {pressure_data}')

sum_picked = 0

for element in pressure_data:
    if (pressure_data.index(element % 2 != 0)) and (element < 65):    
        print(f'Index {pressure_data.index(element)}: value is pressure_data[element]')

print(f'Sum of selected elements is: {sum_picked}')

'''
Level 3
List sequence_data contains integers read from input, representing a sequence of data values. For each index i of sequence_data from 1 through the second-to-last index:

    The element at index i is a bulge if the element is greater than both the preceding element and the following element.
    If the element at index i is a bulge, then output 'Bulge: ', followed by the preceding element, the current element, and the following element, separating each element by a space.

Click here for example
Ex: If the input is 20 39 31 51 90, then the output is:
Sequence: [20, 39, 31, 51, 90]
Bulge: 20 39 31
Note: sequence_data always has at least three elements.
'''
# Read input and split input into tokens
tokens = input().split()

sequence_data = []
for token in tokens:
    sequence_data.append(int(token))

print(f'Sequence: {sequence_data}')


for index in range(1, len(sequence_data) - 1):
    if (sequence_data[index] > sequence_data[index-1]) and (sequence_data[index] > sequence_data[index+1]):
        print(f'Bulge: {sequence_data[index-1]} {sequence_data[index]} {sequence_data[index+1]}')
    


