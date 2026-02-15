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
color_dict: dict[str, str | int] = {
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
Perform the following tasks:

Read string customer_name from input.
Create a list containing values 'corn' and 'radish', in that order.
Add a new key-value pair to customers_order with customer_name as the key and the list as the value.

Click here to show example
Ex: If the input is Kim, then the output is:
Kim: ['corn', 'radish']
'''
customers_order = {}

customer_name = input()
order_list = ['corn','radish']

customers_order[customer_name] = order_list

print(f'{customer_name}: {customers_order[customer_name]}')

'''
Level 3
Integer num_data is read from input, representing the number of remaining strings in the input. Use a for loop to read the remaining strings from input. Each string consists of a key string and a value string separated by a space. Add each key-value pair into the dictionary contact_dict.

Click here to show example
Ex: If the input is:
2
Abe abe@peach.org
Tia tia@milk.org
then the output is:
Contact dict:
{'Abe': 'abe@peach.org', 'Tia': 'tia@milk.org'}
'''
contact_dict = {}
num_data = int(input())

for i in range(num_data):
    new_entry = input()
    key_read,value_read = new_entry.split(' ')
    contact_dict[key_read] = value_read

print('Contact dict:')
print(contact_dict)

'''
Level 4
Read strings from input until 'quit' is read. For each string read:
    If the string is a key in dictionary contact_dict, delete the key from contact_dict.
    Otherwise, output the string followed by ' not in dict'.

Click here to show example
Ex: If the input is:
Mia
Bob
Eve
quit

then the output is:
Mia not in dict
Eve not in dict
Updated contact dict:
{'Ina': 'ina@milk.org', 'Dax': 'dax@butter.com'}
'''
contact_dict = {'Ina': 'ina@milk.org', 'Bob': 'bob@plum.org', 'Dax': 'dax@butter.com'}

user_input = input()

while user_input != 'quit':
    if user_input == 'quit':
        break
    elif user_input in contact_dict:
        del contact_dict[user_input]
    else:
        print(f'{user_input} not in dict')
    user_input = input()

print('Updated contact dict:')
print(contact_dict)