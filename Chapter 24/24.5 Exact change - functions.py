'''
Define a function called exact_change that takes the total change amount in cents and calculates the change using the fewest coins. The coin types are pennies, nickels, dimes, and quarters. Then write a main program that reads the total change amount as an integer input, calls exact_change(), and outputs the change, one coin type per line. Use singular and plural coin names as appropriate, like 1 penny vs. 2 pennies. Output "no change" if the input is 0 or less.

Ex: If the input is:
    0 
(or less), the output is:
    no change

Ex: If the input is:
    45
the output is:
    2 dimes 
    1 quarter

Your program must define and call the following function. The function exact_change() should return a tuple containing num_pennies, num_nickels, num_dimes, and num_quarters.
def exact_change(user_total)
'''
def exact_change(user_total):
    num_quarters = user_total // 25
    remaining = user_total % 25

    num_dimes = remaining // 10
    remaining = remaining % 10

    num_nickels = remaining // 5
    remaining = remaining % 5

    num_pennies = remaining 

    return num_pennies, num_nickels, num_dimes, num_quarters

if __name__ == '__main__': 
    input_val = int(input())    

    if input_val <= 0:
        print("no change")
    else:
        num_pennies, num_nickels, num_dimes, num_quarters = exact_change(input_val)

        if num_pennies > 0:
            if num_pennies == 1:
                print("1 penny")
            else:
                print(f"{num_pennies} pennies")

        if num_nickels > 0:
            if num_nickels == 1:
                print("1 nickel")
            else:
                print(f"{num_nickels} nickels")

        if num_dimes > 0:
            if num_dimes == 1:
                print("1 dime")
            else:
                print(f"{num_dimes} dimes")

        if num_quarters > 0:
            if num_quarters == 1:
                print("1 quarter")
            else:
                print(f"{num_quarters} quarters")