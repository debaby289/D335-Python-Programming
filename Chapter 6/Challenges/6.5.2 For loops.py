'''
Challenge : For loops
Level 1
Integer val_count is read from input representing the number of values to be read next. The remaining values are read from input into color_list. For each value in color_list, output the value followed by ' chosen' on the same line.
'''
val_count = int(input())
color_list = []
for i in range(val_count):
    color_list.append(input())

print(f'List has {val_count} elements:')

for color in color_list:
    print(f'{color} chosen')

'''
Level 2
Integer input_count is read from input representing the number of values to be read next. The remaining values are read from input into color_list. Use a for loop to output all values in color_list on the same line, and surround each value with square brackets '[' and ']'. After the loop terminates, output a newline.
'''
input_count = int(input())
color_list = []
for i in range(input_count):
    color_list.append(input())

print(f'List has {input_count} elements:')

for color in color_list:
    print(f'[{color}]', end='')
print() 

'''
Level 3
state_dict is a dictionary with states' name and code pairs. A new state is read from input and added into state_dict. For each state in state_dict, output the state's name, followed by "'s code: ", and the state's code.
'''
state_dict = {
    'New Hampshire': 'NH',
    'Florida': 'FL',
    'North Carolina': 'NC',
    'Oregon': 'OR',
    'Texas': 'TX'
}

state_name = input()
state_code = input()
state_dict[state_name] = state_code

for state in state_dict:
    print(f"{state}'s code: {state_dict[state]}")