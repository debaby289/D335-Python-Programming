'''
Challenge : List slicing
Level 1
List countries_list is read from input. Assign selected_countries with a slice of countries_list from the first element up to and excluding the last three elements.

Click here for example
Ex: If the input is:
Peru Russia Benin Nauru Vietnam

then the output is:
Original list of countries: ['Peru', 'Russia', 'Benin', 'Nauru', 'Vietnam']
Selected list of countries: ['Peru', 'Russia']
'''
countries_list = input().split()

selected_countries = countries_list[0:-3]

print(f'Original list of countries: {countries_list}')
print(f'Selected list of countries: {selected_countries}')

'''
Level 2
List signals_data is read from input. The elements of signals_data are separated into quarters. The first, second, third, and fourth quarters of the signal data are signal strengths collected at four different bandwidths, respectively. Integer slice_length represents the number of signal strengths in each bandwidth.
    Assign slice_length with len(signals_data) // 4.

    Assign signals_bandwidth1 with a slice of signals_data from the beginning up to and excluding index slice_length.

    Assign signals_bandwidth2 with a slice of signals_data from index slice_length up to and excluding index (2 * slice_length).

    Assign signals_bandwidth3 with a slice of signals_data from index (2 * slice_length) up to and excluding index (3 * slice_length).

    Assign signals_bandwidth4 with a slice of signals_data from index (3 * slice_length) up to and including the end.

Click here for example
Ex: If the input is:
34 93 77 87 66 22 74 67

then the output is:
Number of signal strengths in each bandwidth: 2
All signals collected: [34, 93, 77, 87, 66, 22, 74, 67]
Signals in bandwidth 1: [34, 93]
Signals in bandwidth 2: [77, 87]
Signals in bandwidth 3: [66, 22]
Signals in bandwidth 4: [74, 67]
'''
signals_data = []
for token in input().split():
	signals_data.append(int(token))

slice_length = len(signals_data) // 4

signals_bandwidth1 = signals_data[0:slice_length]
signals_bandwidth2 = signals_data[slice_length:2*slice_length]
signals_bandwidth3 = signals_data[2*slice_length:3*slice_length]
signals_bandwidth4 = signals_data[3*slice_length:]

print(f'Number of signal strengths in each bandwidth: {slice_length}')
print(f'All signals collected: {signals_data}')
print(f'Signals in bandwidth 1: {signals_bandwidth1}')
print(f'Signals in bandwidth 2: {signals_bandwidth2}')
print(f'Signals in bandwidth 3: {signals_bandwidth3}')
print(f'Signals in bandwidth 4: {signals_bandwidth4}')

'''
Level 3
List grocery_list is read from input. Perform the following tasks:
Assign backup_copy with a copy of grocery_list using [:].
Assign selected_items with a slice of grocery_list that includes all the elements at the even indices of grocery_list.

Click here for example
Ex: If the input is:
lime wrap cake mango

then the output is:
Backup grocery items: ['lime', 'wrap', 'cake', 'mango']
Selected grocery items: ['lime', 'cake']
'''
grocery_list = input().split()

backup_copy = grocery_list[:]
selected_items = grocery_list[0::2]

grocery_list.clear()
print(f'Backup grocery items: {backup_copy}')
print(f'Selected grocery items: {selected_items}')
