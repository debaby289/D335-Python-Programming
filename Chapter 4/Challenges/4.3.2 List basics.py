'''
Challenge 3: List basics
Level 1
Two costs are read from input into variables cost1 and cost2. Create a list named costs_list to hold cost1 and cost
'''
cost1 = float(input())
cost2 = float(input())

costs_list = [cost1,cost2]

print(costs_list)

'''
Level 2
List state_codes_list is created with two state codes read from input. Then, list cities_list is created with two cities read from input. On one line, output:
    cities_list's second element
    a comma and a space (', ')
    state_codes_list's second element
'''
# Reads two values from input into state_codes_list
state_codes_list = [input(), input()]
# Reads two values from input into cities_list
cities_list = [input(), input()]

print(f'{cities_list[1]}, {state_codes_list[1]}')
'''
Level 3
List years_list is created with the first three integers read from input. Remove the second element of years_list. Then, read an additional integer from input and append the integer to years_list.
'''
# Reads three values from input into years_list
years_list = [int(input()), int(input()), int(input())]

years_list.pop(1)
years_list.append(int(input()))

print(years_list)

'''
Level 4
List data_list is created with three integers read from input. Using list methods and/or functions, assign:
    index_var with the index of the element 13 in data_list.
    len_var with the length of data_list.
    min_var with the smallest value in data_list.
    max_var with the largest element of data_list.
'''
# Reads three values from input into data_list
data_list = [int(input()), int(input()), int(input())]

index_var = data_list.index(13)
len_var = len(data_list)
min_var = min(data_list)
max_var = max(data_list)

print(f'13 is found at index {index_var} of {data_list}')
print(f'List length: {len_var}')
print(f'Min: {min_var}')
print(f'Max: {max_var}')