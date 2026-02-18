'''
Challenge : 
Level 1
The Pet class constructor has a self parameter and three additional parameters: color, type, and name. Input values color1, type1, and name1 are read representing the information of a pet. Instantiate a new instance of Pet by assigning pet1 with an instance of Pet with color1 as color, type1 as type, and name1 as name.

Click here for example
Ex: If the input is:
    cream
    dog
    Koda

then the output is:
    pet1 data: cream, dog, Koda
'''
class Pet1:
    def __init__(self, color, type, name):
        self.color = color
        self.type = type
        self.name = name

color1 = input()
type1 = input()
name1 = input()

pet1 = Pet1(color1, type1, name1)

print(f'pet1 data: {pet1.color}, {pet1.type}, {pet1.name}')

'''
Level 2
The Pet class constructor has a self parameter and three additional parameters: name, breed, and age. pet1 is created with 'Scout', 'Cockatiel', and 23 as the values of the three attributes in that order. pet2 is created with the values of the three attributes read from input. Complete the constructor so the instance attributes are assigned.

Click here for example
Ex: If the input is:
    Scout
    Parakeet
    17

then the output is:
    pet1 data: Scout, Cockatiel, 23 months old
    pet2 data: Scout, Parakeet, 17 months old
'''
class Pet:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

name2 = input()
breed2 = input()
age2 = int(input())

pet1 = Pet('Scout', 'Cockatiel', 23)
pet2 = Pet(name2, breed2, age2)

print(f'pet1 data: {pet1.name}, {pet1.breed}, {pet1.age} months old')
print(f'pet2 data: {pet2.name}, {pet2.breed}, {pet2.age} months old')

'''
Level 3
Write an __init__ method that requires four parameters in addition to the self parameter:
    The first parameter has no default value.
    The second parameter has no default value.
    The third parameter has -1 as the default value.
    The fourth parameter has -1 as the default value.
In the __init__ method, assign instance attributes:
    seat with the first parameter.
    name with the second parameter.
    num_checked_bags with the third parameter.
    plane_num with the fourth parameter.

Click here for example
Ex: If the input is:
    8G
    Lachlan Ford
    4
    9501
then the output is:
    Default passenger data: seat 11A, Carlos Roy, -1 checked bags, Flight #-1
    passenger2 data: seat 8G, Lachlan Ford, 4 checked bags, Flight #9501
'''
class Passenger3:
    def __init__(self,seat,name,num_checked_bags=-1,plane_num=-1):
        self.seat = seat
        self.name = name
        self.num_checked_bags = num_checked_bags
        self.plane_num = plane_num

seat2 = input()
name2 = input()
num_checked_bags2 = int(input())
plane_num2 = int(input())

default_passenger = Passenger3('11A', 'Carlos Roy')
passenger2 = Passenger3(seat2, name2, num_checked_bags2, plane_num2)

print(f'Default passenger data: seat {default_passenger.seat}, {default_passenger.name}, {default_passenger.num_checked_bags} checked bags, Flight #{default_passenger.plane_num}')
print(f'passenger2 data: seat {passenger2.seat}, {passenger2.name}, {passenger2.num_checked_bags} checked bags, Flight #{passenger2.plane_num}')

'''
Level 4
Input values airport_code1, plane_num1 and name1 are read from input, representing the airport code, plane number, and name of a passenger. An element representing a new airport_code is also read from input as new_dest. Complete the following tasks:
    Assign passenger1 with an instance of Passenger with airport_code1, plane_num1 and name1 as attributes in that order.
    Call passenger1's print_data().
    Call passenger1's update_destination() with argument new_dest.
    Call passenger1's print_data() again.

Click here for example
Ex: If the input is:
    LAX
    7501
    Maryam Cole
    YVR
then the output is:
    Passenger data: flying to LAX, Flight #7501, Maryam Cole
    Passenger data: flying to YVR, Flight #7501, Maryam Cole
'''
class Passenger:
    def __init__(self, airport_code, plane_num, name): 
        self.airport_code = airport_code
        self.plane_num = plane_num
        self.name = name

    def update_destination(self, new_dest):
        self.airport_code = new_dest

    def print_data(self):
        print(f'Passenger data: flying to {self.airport_code}, Flight #{self.plane_num}, {self.name}')

airport_code1 = input()
plane_num1 = int(input())
name1 = input()
new_dest = input()

passenger1 = Passenger(airport_code1,plane_num1,name1)
passenger1.print_data()
passenger1.update_destination(new_dest)
passenger1.print_data()

