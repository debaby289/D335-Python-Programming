'''
Challenge : Iterating over a dictionary
Level 1
Multiple key-value pairs, each representing a person's name and email address, are read from input and added to contact_dict. Convert contact_dict's items into a list and then sort the list. Assign sorted_items with the sorted list.

Click here for example
Ex: If the input is:
Ina zebra5@corn.com
Gus user2@berry.com
exit
then the output is:
[('Gus', 'user2@berry.com'), ('Ina', 'zebra5@corn.com')]
'''
contact_dict = {}

input_line = input()
while input_line != 'exit':
    name, email = input_line.split()
    contact_dict[name] = email
    input_line = input()

sorted_items = sorted(contact_dict.items())

print(sorted_items)

'''
Level 2
Multiple key-value pairs, each representing a hotel room number and current temperature, are read from input and added to room_temperatures. In sorted order of the keys, output each key-value pair that has a key greater than 400. Begin each output with the key followed by the value, separated by a space.

Click here for example
Ex: If the input is:
450 73.7
400 74.2
350 71.0
done

then the output is:

450 73.7
'''
room_temperatures = {}

input_line = input()
while input_line != 'done':
    room_number, temp = input_line.split()
    room_temperatures[int(room_number)] = float(temp)
    input_line = input()

for room_num,temp  in sorted(room_temperatures.items()):
    if room_num > 400:
        print(f'{room_num} {temp}')
