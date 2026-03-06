'''
Given the number of people attending a pizza party, output the number of people, number of pizzas needed, and the total cost for the number of pizzas. For the calculation, assume that people eat 2 slices on average and each pizza has 12 slices and costs $14.95.

Output each floating-point value with two digits after the decimal point using the following statement:
print(f'Cost for {num_pizzas} pizza(s): ${cost:.2f}')

Hint: Use the ceil() function from the math module to round up the number of pizzas so that enough pizzas are ordered.

Ex: If the input is:
    20

the output is:
    People: 20
    Pizza(s): 4
    Cost for 4 pizza(s): $59.80
'''
import math

people = int(input())
slices = 2 * people
pizza = slices / 12

num_pizzas = math.ceil(pizza)
cost = 14.95 * num_pizzas

print(f'People: {people}')
print(f'Pizza(s): {num_pizzas}')
print(f'Cost for {num_pizzas} pizza(s): ${cost:.2f}')