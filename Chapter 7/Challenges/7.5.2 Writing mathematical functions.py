'''
Challenge : Writing mathematical functions
Level 1
Complete the function fluid_ounces_to_milliliters() that has one parameter as a volume in fluid ounces. The function returns the volume converted to milliliters, given that 1 fluid ounce = 29.5735 milliliters.

Ex: If the input is 34, then the output is:
The number of milliliters is 1005.499
'''
def fluid_ounces_to_milliliters(user_fluid_ounces):
    return user_fluid_ounces * 29.5735

num_fluid_ounces = int(input())
  
# Print with value rounded to 3 decimal places  
print(f'The number of milliliters is {fluid_ounces_to_milliliters(num_fluid_ounces):.3f}')

'''
Level 2
Define a function convert_volume() that has two parameters as the number of cups and fluid ounces. The function returns the volume converted to liters, given that:

1 fluid ounce = 0.0295735 liters
1 cup = 8 fluid ounces

Ex: If the input is:
3
69

then the output is:
The number of liters is 2.750
'''
LITERS_PER_FLUID_OUNCE = 0.0295735
FLUID_OUNCES_PER_CUP = 8

def convert_volume(num1,num2):
    cup_to_oz = num1 * FLUID_OUNCES_PER_CUP
    flz_to_liters = (cup_to_oz + num2) * LITERS_PER_FLUID_OUNCE
    return flz_to_liters
   
user_cups = int(input())
user_fluid_ounces = int(input())

# Print with value rounded to 3 decimal places  
print(f'The number of liters is {convert_volume(user_cups, user_fluid_ounces):.3f}')

'''
Level 3
Define the following functions:

find_base_area() has one parameter as a cone's radius. The function returns the area of the cone's base. The area of the base is calculated by:

find_volume() has two parameters as a cone's radius and height. The function returns the cone's volume, and uses the find_base_area() function to calculate the cone's base area. The volume is calculated by:

Click here for example
Ex: If the input is:
2.0
5.0

then the output is:
Cone radius: 2.0
Cone height: 5.0
Base area: 12.6
Volume: 20.9

Note: Use math.pi for pi
'''
import math

def find_base_area(rad):
    area = math.pi * math.pow(rad,2)
    return area

def find_volume(rad,height):
    volume = find_base_area(rad) * height * (1/3)
    return volume

cone_radius = float(input())
cone_height = float(input())

print(f'Cone radius: {cone_radius}')
print(f'Cone height: {cone_height}')
print(f'Base area: {find_base_area(cone_radius):.1f}')
print(f'Volume: {find_volume(cone_radius, cone_height):.1f}')
