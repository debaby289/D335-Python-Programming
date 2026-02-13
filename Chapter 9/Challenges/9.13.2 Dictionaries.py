'''
Challenge : Dictionaries
Level 1
Perform the following tasks:
    Create a dictionary named color_dict containing key-value pairs 'red': 0, 'green': 0, and 'blue': 128.
    Read strings key_read and value_read from input.
    Add key_read and value_read as a new key-value pair to color_dict with key_read as the key and value_read as the value.

Click here to show example
Ex: If the input is:
name
navy

then the output is:
red: 0
green: 0
blue: 128
name: navy
'''
color_dict = {
    'red': 0,
    'green': 0,
    'blue': 128
}

key_read = input()
value_read = input()

color_dict[key_read] = value_read

print(f'red: {color_dict["red"]}')
print(f'green: {color_dict["green"]}')
print(f'blue: {color_dict["blue"]}')
print(f'{key_read}: {color_dict[key_read]}')

'''
Level 2

'''


'''
Level 3

'''

'''
Level 4

'''
