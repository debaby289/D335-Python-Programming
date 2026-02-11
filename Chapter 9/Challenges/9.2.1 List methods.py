'''
Challenge : List methods
Level 1
Integer num_appointments is read from input, representing the number of strings to be read next. Read the remaining strings from input and insert each string at the front of appointments_list at position 0.

Click here for example
Ex: If the input is:
3
3/22
1/27
9/26
then the output is:
['9/26', '1/27', '3/22']
'''
num_appointments = int(input())

appointments_list = []

for i in range(num_appointments):
    appointment = input()
    appointments_list.append(appointment)

appointments_list.reverse()

print(appointments_list)

'''
Level 2
Lists not_on_board and on_board are read from input, representing passengers waiting to board a bus and passengers on the bus, respectively. Perform the following tasks:
    Remove the last element from not_on_board and output 'Passenger left bus stop: ' followed by the element.
    Add all the remaining elements of not_on_board to the end of on_board.

Click here for example
Ex: If the input is:
Guy Zoe Pat
Fay Sue

then the output is:
Passengers waiting at a bus stop: ['Guy', 'Zoe', 'Pat']
Passengers on board: ['Fay', 'Sue']
Passenger left bus stop: Pat
Updated passengers on board: ['Fay', 'Sue', 'Guy', 'Zoe']

Note: All passenger names are unique.
'''
not_on_board = input().split()
on_board = input().split()

print(f'Passengers waiting at a bus stop: {not_on_board}')
print(f'Passengers on board: {on_board}')
print(f'Passenger left bus stop: {not_on_board[-1]}')

not_on_board.pop()
on_board = on_board + not_on_board

print(f'Updated passengers on board: {on_board}')

'''
Level 3
List values_list is read from input, representing a data sequence collected from an experiment. List values_list has an odd number of elements. Perform the following tasks:
    Sort values_list in-place.
    Assign median_index with the size of values_list divided by 2 using floor division.
    Assign sample_median with the value at median_index in values_list.

Click here for example
Ex: If the input is 17 27 42 14 43, then the output is:
Sorted data: [14, 17, 27, 42, 43]
Median: 27
'''
tokens = input().split()
values_list = []
for token in tokens:
    values_list.append(int(token))

values_list.sort()

median_index = len(values_list) // 2
sample_median = values_list[median_index]

print(f'Sorted data: {values_list}')
print(f'Median: {sample_median}')
