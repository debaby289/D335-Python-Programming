'''
Challenge : 4.4.1: Tuple basics.
Level 1
A tuple named color_info is created with one string and three integers read from input as color_info's fields. Output color_info's four fields in the same order that the fields are read. End each output with a newline.
'''
color_info = (input(), int(input()), int(input()), int(input()))

for colors in color_info:
    print(colors)

'''
Level 2
Four values are read from input and are stored into variables color_name, red_channel, green_channel, and blue_channel. Initialize a tuple named color_info to store color_name, red_channel, green_channel, and blue_channel, in that order.
'''
color_name = input()
red_channel = int(input())
green_channel = int(input())
blue_channel = int(input())

color_info = (color_name,red_channel,green_channel,blue_channel)
print(f'Color name: {color_info[0]}, R: {color_info[1]}, G: {color_info[2]}, B: {color_info[3]}')

'''
Level 3
Import the namedtuple container from collections. Then, define a named tuple called Color with fields: name, R, G, and B, in that order.
'''
from collections import namedtuple

Color = namedtuple('Car', ['name', 'R', 'G', 'B'])  

color_name = input()
red_channel = int(input())
green_channel = int(input())
blue_channel = int(input())

color = Color(color_name, red_channel, green_channel, blue_channel)

print(f'Color name: {color.name}, R: {color.R}, G: {color.G}, B: {color.B}')

'''
Level 4
City is a named tuple with fields: name, state, and population. Read two strings and one integer from input. Create city_info as a City tuple, and initialize city_info with city_name, state_located, and population_count as the fields.
'''
from collections import namedtuple

City = namedtuple('City', ['name', 'state', 'population'])

city_name = input()
state_located = input()
population_count = int(input())

city_info = City(city_name,state_located,population_count)

print(f'City name: {city_info.name}, State: {city_info.state}, Population: {city_info.population}')