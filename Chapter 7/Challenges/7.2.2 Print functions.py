'''
Challenge : Print functions
Level 1
Two name-salary pairs are read from input and are passed as arguments for print_user_salary(). Define a function print_user_salary() that has two parameters and outputs the following all on one line:

the value of the first parameter
' earns '
the value of the second parameter
' dollars per year.'
print_user_salary() should not return any value.

Click here for example
Ex: If the input is:
Maricruz
47600
Santino
37000

then the output is:
Maricruz earns 47600 dollars per year.
Santino earns 37000 dollars per year.
'''
def print_user_salary(take1,take2):
    print(f'{take1} earns {take2} dollars per year.')

user_name1 = input()
user_salary1 = int(input())
user_name2 = input()
user_salary2 = int(input())

print_user_salary(user_name1, user_salary1)
print_user_salary(user_name2, user_salary2)

'''
Level 2
Six foods are read from input. Define a function print_product_list() that has three parameters and outputs:

'Product list:' on the first line.
'- ', followed by the value of the first parameter on the second line.
'- ', followed by the value of the second parameter on the third line.
'- ', followed by the value of the third parameter on the fourth line.
print_product_list() should not return any value.

Click here for example
Ex: If the input is:
lobster
papaya
clam
crawfish
yam
tipalia

then the output is:
Product list:
- lobster
- papaya
- clam
Product list:
- crawfish
- yam
- tipalia
'''
def print_product_list(take1,take2,take3):
    print(f'Product list:')
    print(f'- {take1}')
    print(f'- {take2}')
    print(f'- {take3}')

product1 = input()
product2 = input()
product3 = input()
product4 = input()
product5 = input()
product6 = input()

print_product_list(product1, product2, product3)
print_product_list(product4, product5, product6)

'''
Level 3
Define a function print_division_of_2() that has two parameters, and outputs 'Outcome: ' followed by the result of dividing the first parameter by the second parameter with a precision of two digits. print_division_of_2() should not return any value.

Click here for example
Ex: If the input is:
28.00
14.00
36.00
12.00

then the output is:
Outcome: 2.00
Outcome: 3.00

Note:
The calculation to find the division of two values x and y is (x / y).
print(f'{my_float:.2f}') outputs my_float with a precision of two digits.
The denominator is always non-zero.
'''
def print_division_of_2(take1,take2):
    print(f'Outcome: {(take1 / take2):.2f}')

a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

print_division_of_2(a1, b1)
print_division_of_2(a2, b2)
'''
Level 4
Read in four values from input and call print_product_rate() twice: once with the first and third inputs as arguments, and again with the second and fourth inputs as arguments.

Click here for example
Ex: If the input is:
turkey
korma
16
23

then the output is:
One turkey costs 16 dollars.
One korma costs 23 dollars.
'''
def print_product_rate(food_name, price):
    print(f'One {food_name} costs {price} dollars.')

a1 = input()
b1 = input()
c1 = input()
d1 = input()

print_product_rate(a1,c1)
print_product_rate(b1,d1)