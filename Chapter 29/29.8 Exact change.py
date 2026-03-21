'''
Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Ex: If the input is:
    0 
(or less than 0), the output is:
     

Ex: If the input is:
    45
the output is:
    1 Quarter
    2 Dimes 
'''
#Starting
change = int(input())

#Coin types
dollar_coin = 100
quarter_coin = 25
dime_coin = 10
nickel_coin = 5
penny_coin = 1

#Zero or less Check
if change <= 0:
    print('No change')
#Value Check
else:
    #Dollars
    num_dollar = change // dollar_coin
    holding_val = change % dollar_coin

    #Quarters
    num_quarter = holding_val // quarter_coin
    holding_val = holding_val % quarter_coin

    #Dimes 
    num_dimes = holding_val // dime_coin
    holding_val = holding_val % dime_coin

    #Nickels 
    num_nickels = holding_val // nickel_coin
    holding_val = holding_val % nickel_coin

    #Pennies 
    num_pennies = holding_val

    #Output desc order
    if num_dollar > 0:
        if num_dollar == 1:
            print('1 Dollar')
        else:
            print(f'{num_dollar} Dollars')

    if num_quarter > 0:
        if num_quarter == 1:
            print('1 Quarter')
        else:
            print(f'{num_quarter} Quarters')

    if num_dimes > 0:
        if num_dimes == 1:
            print('1 Dime')
        else:
            print(f'{num_dimes} Dimes')

    if num_nickels > 0:
        if num_nickels == 1:
            print('1 Nickel')
        else:
            print(f'{num_nickels} Nickels')

    if num_pennies > 0:
        if num_pennies == 1:
            print('1 Penny')
        else:
            print(f'{num_pennies} Pennies')
