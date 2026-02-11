'''
Challenge : Splitting and joining strings
Level 1
String athlete_names is read from input. Split athlete_names into tokens using a period (".") as the separator and assign athletes_list with the result.

Ex: If the input is Noemi.Asha.Enrique, then the output is:

['Noemi', 'Asha', 'Enrique']
'''
athlete_names = input()

athletes_list = athlete_names.split('.')

print(athletes_list)

'''
Level 2
Strings all_colors and updated_value are read from input. Perform the following tasks:

Split all_colors into tokens using the default separator and assign color_list with the result.
Replace the first element in color_list with updated_value.

Click here for example
Ex: If the input is:
yellow coral purple
gold

then the output is:
['gold', 'coral', 'purple']
'''
all_colors = input()
updated_value = input()

color_list = all_colors.split()
color_list[0] = updated_value

print(color_list)

'''
Level 3
List bens_list is read from input. 
Join the strings in bens_list together to create a single string with " or " as the separator and assign all_colors with the result.

Ex: If the input is yellow gold coral green, then the output is:

Ben's colors: yellow or gold or coral or green
'''

bens_list = input().split()

all_colors = ' or '.join(bens_list)

print(f"Ben's colors: {all_colors}")