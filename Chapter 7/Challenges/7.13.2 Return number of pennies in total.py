'''
Docstring for Chapter 7.Challenges.7.13.2 Return number of pennies in total
Given that 1 dollar = 100 pennies, write a function number_of_pennies() that takes two arguments: the number of dollars, and an optional number of pennies. number_of_pennies() should return the total number of pennies.

The code reads three values from input and calls number_of_pennies() twice.
Ex: If the input is 5 6 4, number_of_pennies() is first called with arguments 5 and 6, representing $5.06, and then number_of_pennies() is only called with argument 4, representing $4.00.

Then the output is:
506
400
'''
def number_of_pennies(num_doll,optional_penns = 0):
    penns = num_doll * 100
    penns = penns + optional_penns
    return penns

print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
print(number_of_pennies(int(input())))               # Dollars only