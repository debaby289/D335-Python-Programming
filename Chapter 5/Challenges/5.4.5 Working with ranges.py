'''
Challenge : Working with ranges
Level 1
When the input variable num_bikes is:
    less than 20, output 'Small bike rack'.
    between 20 inclusive and 48 inclusive, output 'Mid-sized bike rack'.
    greater than 48, output 'Need multiple racks'.
'''
num_bikes = int(input())

if num_bikes < 20:
    print('Small bike rack')
elif 20 <= num_bikes <= 48:
    print('Mid-sized bike rack')
else:
    print('Need multiple racks')
    
'''
Level 2
When the input variable fish_count is:
    greater than or equal to 11, output 'Too many fish'.
    between 7 inclusive and 11 exclusive, output 'Jumbo aquarium'.
    between 1 inclusive and 6 inclusive, output 'Mid-sized aquarium'.
    less than 1, output 'Invalid number'.
'''
fish_count = int(input())

if fish_count >= 11:
    print('Too many fish')
elif 7 <= fish_count <= 11:
    print('Jumbo aquarium')
elif 1 <= fish_count <= 11:
    print('Mid-sized aquarium')
elif fish_count < 1:
    print('Invalid number')
