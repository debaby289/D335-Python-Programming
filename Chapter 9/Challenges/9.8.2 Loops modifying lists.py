'''
Challenge : Loops modifying lists
Level 1
List data_list contains integers read from input. Each integer represents an experiment's data in meters. Write a loop to update each element in data_list with the element's value multipled by 100.

Click here for example
Ex: If the input is 16 46 10 27, then the output is:

Values in meters: 16 46 10 27 
Values in centimeters: 1600 4600 1000 2700 
'''
data_list = []

tokens = input().split()
for token in tokens:
    data_list.append(int(token))
  
print('Values in meters:', end=' ')
for data in data_list:
    print(data, end=' ')
print()

for i in range(len(data_list)):
    data_list[i] = data_list[i] * 100  

print('Values in centimeters:', end=' ')
for data in data_list:
    print(data, end=' ')
print()

'''
Level 2
List ages_list contains integers read from input. Each integer represents a patient's age in a drug trial. Write a loop to remove every element from ages_list that is less than 35 or greater than 65.

Click here for example
Ex: If the input is 65 35 10 31, then the output is:

Original ages: 65 35 10 31 
Screened ages: 65 35 
Note:
    Iterate over a copy of the list using slice notation.
    The logical test ((x < 35) or (x > 65)) returns true if x is less than 35 or greater than 65.
'''
ages_list = []

tokens = input().split()
for token in tokens:
    ages_list.append(int(token))
  
print('Original ages:', end=' ')
for age in ages_list:
    print(age, end=' ')
print()

for age in ages_list[:]:  
    if (age < 35) or (age > 65):
        ages_list.remove(age)  

print('Screened ages:', end=' ')
for age in ages_list:
    print(age, end=' ')
print()

'''
Level 3
List food_on_menu contains words read from the first line of input. List favorite_food contains words read from the second line of input. For each element in food_on_menu that is not in favorite_food:
    Output the element, followed by ' not ordered'.
    Remove the element from food_on_menu.

Click here for example
Ex: If the input is:
apricot mushroom onion grape
apple apricot mushroom
then the output is:
Food on menu: apricot mushroom onion grape 
Favorite food: apple apricot mushroom 
onion not ordered
grape not ordered
Want to eat: apricot mushroom 
'''

food_on_menu = input().split()
favorite_food = input().split()
  
print('Food on menu:', end=' ')
for food in food_on_menu:
    print(food, end=' ')
print()

print('Favorite food:', end=' ')
for food in favorite_food:
    print(food, end=' ')
print()

for food in food_on_menu[:]:
    if food not in favorite_food:
        print(f'{food} not ordered')
        food_on_menu.remove(food)

print('Want to eat:', end=' ')
for food in food_on_menu:
    print(food, end=' ')
print()
