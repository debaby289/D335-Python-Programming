'''
Challenge : Type conversions
Level 1
A string is read from input into variable num_units. Use a conversion function to convert the value of num_units to an integer and assign the value to the variable int_units.
'''
num_units = input()
int_units = int(num_units)

print(int_units + 7)

'''
Level 2
Given that 1 tablespoon = 3 teaspoons, complete the multiplication of num_tablespoons and TEASPOONS_PER_TABLESPOON so that the result is implicitly converted to a float.
'''
TEASPOONS_PER_TABLESPOON = 3
num_tablespoons = float(input())

num_teaspoons = num_tablespoons * TEASPOONS_PER_TABLESPOON

print(f'{num_teaspoons} teaspoons')

'''
Level 3
Three integers are read from input into variables num_kilometers1, num_kilometers2, and num_kilometers3. Assign avg_kilometers_per_hour with the average kilometers per hour. Then, convert avg_kilometers_per_hour to an integer.
'''
num_kilometers1 = int(input())
num_kilometers2 = int(input())
num_kilometers3 = int(input())

avg_kilometers_per_hour = int((num_kilometers1 + num_kilometers2 + num_kilometers3) / 3)

print(avg_kilometers_per_hour)
