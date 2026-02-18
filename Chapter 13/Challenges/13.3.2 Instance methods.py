'''
Challenge : 
Level 1
credit1 and credit2 are instances of the CreditCard class. Attributes month and year of both credit1 and credit2 are read from input. In the CreditCard class, define instance method print_expiration_month_year() with self as the parameter to output the following in one line:

The value of attribute month
'/'
The value of attribute year

Click here for example
Ex: If the input is:
4
2028
7
2025

then the output is:
First expiration month and year:
4/2028
Second expiration month and year:
7/2025
'''
class CreditCard:
    def __init__(self):
        self.month = 0
        self.year = 0

    def print_expiration_month_year(self):
        print(f'{self.month}/{self.year}')

credit1 = CreditCard()
credit1.month = int(input())
credit1.year = int(input())

credit2 = CreditCard()
credit2.month = int(input())
credit2.year = int(input())

print(f'First expiration month and year:')
credit1.print_expiration_month_year()
print(f'Second expiration month and year:')
credit2.print_expiration_month_year()

'''
Level 2
point1 and point2 are instances of the Coordinates3D class. Attributes x_coord, y_coord, and z_coord of both point1 and point2 are read from input. In the Coordinates3D class, define instance method print_coordinates() with self and one string as parameters to output the following in one line:

The string parameter
The value of attribute x_coord
', '
The value of attribute y_coord
', '
The value of attribute z_coord

Click here for example
Ex: If the input is:
66
63
89
62
32
96

then the output is:
First location coordinates >>>> 66, 63, 89
Second location coordinates >>>> 62, 32, 96
'''
class Coordinates3D:
    def __init__(self):
        self.x_coord = 0
        self.y_coord = 0
        self.z_coord = 0

    def print_coordinates(self,str):
        print(f'{str}{self.x_coord}, {self.y_coord}, {self.z_coord}')

point1 = Coordinates3D()
point1.x_coord = int(input())
point1.y_coord = int(input())
point1.z_coord = int(input())

point2 = Coordinates3D()
point2.x_coord = int(input())
point2.y_coord = int(input())
point2.z_coord = int(input())

point1.print_coordinates('First location coordinates >>>> ')
point2.print_coordinates('Second location coordinates >>>> ')

'''
Level 3
toy_dispenser1 and toy_dispenser2 are instances of the VendingMachine class. Attribute money_inserted of both toy_dispenser1 and toy_dispenser2 is initialized with 0. In the VendingMachine class, define instance method turn_knob() with self as the parameter to increase attribute money_inserted by 0.5.

Click here for example
Ex: If the input is:
2
3

then the output is:
The first toy dispenser collected $1.00.
The second toy dispenser collected $1.50.
'''
class VendingMachine:
    def __init__(self):
        self.money_inserted = 0

    def turn_knob(self):
        self.money_inserted += 0.5
        return self.money_inserted

toy_dispenser1 = VendingMachine()
for i in range(int(input())):
    toy_dispenser1.turn_knob()
print(f'The first toy dispenser collected ${toy_dispenser1.money_inserted:.2f}.')

toy_dispenser2 = VendingMachine()
for i in range(int(input())):
    toy_dispenser2.turn_knob()
print(f'The second toy dispenser collected ${toy_dispenser2.money_inserted:.2f}.')

