'''
Challenge : Working with branches
Level 1
Integer dog_count is read from input. If dog_count is less than 16, then output dog_count, followed by ' is not enough dogs.'
'''
dog_count = int(input())

if dog_count < 16:
    print(f'{dog_count} is not enough dogs.')

'''
Level 2
Integers num_items and box_capacity are read from input. If num_items is less than or equal to 110, then assign box_capacity with box_capacity minus 110.
'''
num_items = int(input())
box_capacity = int(input())

if num_items <= 110:
    box_capacity  = box_capacity - 110

print(f'box_capacity: {box_capacity}')

'''
Level 3
Integer num_visitors is read from input. If num_visitors is greater than or equal to 12, then output 'A good number of visitors'. Otherwise, output 'Too few visitors'.
'''
num_visitors = int(input())

if num_visitors >= 12:
    print('A good number of visitors')
else:
    print('Too few visitors')

'''
Level 4
Integers number_of_tasks, accepted_groups, and invalid_groups are read from input. If number_of_tasks is greater than 20, then add 5 to accepted_groups. Otherwise, add 2 to invalid_groups.
'''
number_of_tasks = int(input())
accepted_groups = int(input())
invalid_groups = int(input())

if number_of_tasks > 20:
    accepted_groups += 5
else:
    invalid_groups += 2

print(accepted_groups)
print(invalid_groups)