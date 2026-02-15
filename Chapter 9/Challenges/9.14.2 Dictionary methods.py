'''
Challenge : Dictionary methods
Level 1
Multiple key-value pairs, each representing a person's name and food, are read from input and added to favorite_foods1. First, merge favorite_foods2 with favorite_foods1. Then, merge favorite_foods3 with favorite_foods2. Finally, clear favorite_foods1.

Click here for example
Ex: If the input is:
Mel carrot
Ava plum
stop
then the output is:
Favorite foods 1:
{}
Favorite foods 2:
{'Abe': 'apple', 'Dan': 'potato', 'Mel': 'carrot', 'Ava': 'plum'}
Favorite foods 3:
{'Fay': 'mushroom', 'Abe': 'apple', 'Dan': 'potato', 'Mel': 'carrot', 'Ava': 'plum'}
'''
favorite_foods1 = {'Dan': 'potato'}
favorite_foods2 = {'Abe': 'apple'}
favorite_foods3 = {'Fay': 'mushroom'}
ref_record1 = favorite_foods1  # For testing purposes, ref_record1 references favorite_foods1
ref_record2 = favorite_foods2  # For testing purposes, ref_record2 references favorite_foods2
ref_record3 = favorite_foods3  # For testing purposes, ref_record3 references favorite_foods3

input_line = input()
while input_line != 'stop':
	name, food = input_line.split()
	favorite_foods1[name] = food
	input_line = input()

favorite_foods2.update(favorite_foods1)
favorite_foods3.update(favorite_foods2)
favorite_foods1.clear()

print('Favorite foods 1:')
print(favorite_foods1)
print('Favorite foods 2:')
print(favorite_foods2)
print('Favorite foods 3:')
print(str(favorite_foods3))

'''
Level 2
Dictionary vegetables_inspected contains key-value pairs that represent the grade received by each vegetable item in an inspection. Dictionary price_chart contains key-value pairs that represent the recommended price (per pound) of each grade. String vegetables_name is read from input. Complete the following tasks:
    Use pop() to remove vegetables_name from vegetables_inspected and assign vegetables_grade with the value returned. Any string that is not a key in vegetables_inspected has the default value 'unknown'.
    Assign patient_price with the value associated with key vegetables_grade in price_chart. Any number that is not a key in price_chart has default value -1.

Click here for examples
Ex 1: If the input is peas, then the output is:
peas (poor) scores 5.0
Remaining vegetables:
{'garlic': 'great', 'potato': 'good', 'turnip': 'fair'}
Ex 2: If the input is kale, then the output is:
kale (unknown) scores -1
Remaining vegetables:
{'garlic': 'great', 'peas': 'poor', 'potato': 'good', 'turnip': 'fair'}
'''
vegetables_inspected = {'garlic': 'great', 'peas': 'poor', 'potato': 'good', 'turnip': 'fair'}
price_chart = {'great': 50.0, 'good': 40.0, 'fair': 20.0, 'poor': 5.0}

vegetables_name = input()

vegetables_grade = vegetables_inspected.pop(vegetables_name,'unknown')
patient_price = price_chart.get(vegetables_grade,-1)

print(f'{vegetables_name} ({vegetables_grade}) scores {patient_price}')
print('Remaining vegetables:')
print(vegetables_inspected)
