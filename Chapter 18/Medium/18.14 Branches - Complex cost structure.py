'''
An airline describes airfare as follows. A normal ticket's base cost is $300. Persons aged 60 or over have a base cost of $290. Children 2 or under have $0 base cost. A carry-on bag costs $10. A first checked bag is free, second is $25, and each additional is $50. Given inputs of age, carry-on (0 or 1), and checked bags (0 or greater), compute the total airfare.

Hints:
    First use an if-else statement to assign air_fare with the base cost.
    Use another if statement to update air_fare for a carry_on.
    Finally, use another if-else statement to update air_fare for checked bags.
    Think carefully about what expression correctly calculates checked bag cost when bags are 3 or more.
'''
passenger_age = int(input())
carry_ons = int(input())
checked_bags = int(input())
air_fare = 300

# Base ticket price
if passenger_age <= 2:
    air_fare = 0
elif passenger_age >= 60:
    air_fare = 290
else:
    air_fare = 300

#Carry on price
if carry_ons == 1:
    air_fare += 10

#Checked bags price
if checked_bags == 2:
    air_fare += 25
elif checked_bags > 2:
    air_fare = air_fare + (25 + ((checked_bags - 2) * 50))
   
print(air_fare)