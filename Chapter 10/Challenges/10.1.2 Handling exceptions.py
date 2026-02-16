'''
Challenge : 
Level 1
Add a try block that:
Reads integer package_weight from input.
Outputs "Package's weight (in g) is " followed by the value of package_weight.

Click here for example 1 (valid input)
Ex: If the input is 31, then the output is:
Package's weight (in g) is 31

Click here for example 2 (invalid input)
Ex: If the input is R, then the output is:
Error: Input for package's weight is bad
'''
try:
    package_weight  = int(input())

    print(f"Package's weight (in g) is {package_weight}")

except:
    print("Error: Input for package's weight is bad")


'''
Level 2
Add an except block to handle an exception and output 'Error: Your input cannot be processed'.

Click here for example 1 (valid input)
Ex: If the input is 29, then the output is:

Shaft's weight (in g): 29
Click here for example 2 (invalid input)
Ex: If the input is Eli, then the output is:

Error: Your input cannot be processed
'''
try:
    shaft_weight = int(input())
    print(f"Shaft's weight (in g): {shaft_weight}")

# Your code goes here
except:
    print(f'Error: Your input cannot be processed')

'''
Level 3
The while loop reads values from input until three integers are read. Add an except block in the while loop to handle an exception and output 'Discarded bad input value for number of cents'.

Click here for example 1 (valid input)
Ex: If the input is:
150
25
120
10
then the output is:
150 cents = 30 nickels
25 cents = 5 nickels
120 cents = 24 nickels
Processed three valid input values

Click here for example 2 (invalid input)
Ex: If the input is:
Z
150
25
120
10
then the output is:
Discarded bad input value for number of cents
150 cents = 30 nickels
25 cents = 5 nickels
120 cents = 24 nickels
Processed three valid input values
'''
valid_count = 0

while valid_count < 3:
    try:
        num_cents = int(input())
        # num_cents // 5 divides num_cents by 5 using integer division
        print(f'{num_cents} cents = {num_cents // 5} nickels')
        valid_count = valid_count + 1

    except:
        print(f'Discarded bad input value for number of cents')
    
print('Processed three valid input values')


