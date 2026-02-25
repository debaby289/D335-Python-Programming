'''
Given a base Plant class and a derived Flower class, write a program to create a list called my_garden. Store objects that belong to the Plant class or the Flower class in the list. Create a function called print_list(), that uses the print_info() instance methods defined in the respective classes and prints each element in my_garden. The program should read plants or flowers from input (ending with -1), add each Plant or Flower to the my_garden list, and output each element in my_garden using the print_info() function.

Note: A list can contain different data types and also different objects.

Ex. If the input is:

plant Spirea 10 
flower Hydrangea 30 false lilac 
flower Rose 6 false white
plant Mint 4
-1
the output is:

Plant 1 Information:
   Plant name: Spirea
   Cost: 10

Plant 2 Information:
   Plant name: Hydrangea
   Cost: 30
   Annual: false
   Color of flowers: lilac

Plant 3 Information:
   Plant name: Rose
   Cost: 6
   Annual: false
   Color of flowers: white

Plant 4 Information:
   Plant name: Mint
   Cost: 4
'''
class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')

class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')
        print(f'   Annual: { self.is_annual }')
        print(f'   Color of flowers: { self.color_of_flowers }')

def print_list(garden_list):
    for i, plant in enumerate(garden_list, 1):
        print(f'Plant {i} Information:')
        plant.print_info()
        print()

if __name__ == "__main__":
    my_garden = []
    
    user_string = input()
    
    while user_string != '-1':
        parts = user_string.split()
        plant_type = parts[0]
        
        if plant_type == 'plant':
            plant_name = parts[1]
            plant_cost = int(parts[2])
            my_garden.append(Plant(plant_name, plant_cost))
        elif plant_type == 'flower':
            plant_name = parts[1]
            plant_cost = int(parts[2])
            is_annual = parts[3]
            color_of_flowers = parts[4]
            my_garden.append(Flower(plant_name, plant_cost, is_annual, color_of_flowers))
        
        user_string = input()
    
    print_list(my_garden)