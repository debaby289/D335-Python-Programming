'''
Driving is expensive. Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')

Ex: If the input is:
    25.0
    3.1599
where the gas mileage is 25.0 miles/gallon and the cost of gas is $3.1599/gallon, the output is:
    2.53 9.48 63.20

Note: Real per-mile cost would also include maintenance and depreciation.
'''
def gas_to_miles_cost(mileage,cost):
    twenty_miles = (cost * 20) / mileage
    seventy_five_miles = (cost * 75) / mileage
    five_hundred_miles = (cost * 500) / mileage

    return twenty_miles,seventy_five_miles,five_hundred_miles

if __name__ == '__main__':
    gas_mileage = float(input())
    gas_cost = float(input())

    result = gas_to_miles_cost(gas_mileage, gas_cost)
    print(f'{result[0]:.2f} {result[1]:.2f} {result[2]:.2f}')