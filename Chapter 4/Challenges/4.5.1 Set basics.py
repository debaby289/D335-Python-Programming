'''
Challenge : Set basics
Level 1
Create variable unique_animals as an empty set so that three strings can be read from input and added to unique_animals.
'''
unique_animals = set()

animal1 = input()
animal2 = input()
animal3 = input()

unique_animals.add(animal1)
unique_animals.add(animal2)
unique_animals.add(animal3)

print(sorted(unique_animals))

'''
Level 2
Set animals_considered is initialized with three animals read from input. Assign num_animals with the number of elements in animals_considered. Then, clear animals_considered.
'''
animals_considered = set()

new_animal1 = input()
new_animal2 = input()
new_animal3 = input()
animals_considered.add(new_animal1)
animals_considered.add(new_animal2)
animals_considered.add(new_animal3)

num_animals = len(animals_considered)
animals_considered.clear()

print(f'Number of values considered: {num_animals}')
print(sorted(animals_considered))

'''
Level 3
Set names_set1 contains 'Dan'. Set names_set2 contains three strings read from input. Perform the following tasks:
    Update names_set1 with names_set2.
    Read the next string from input and remove the string from names_set1.
    Read the next string from input and add the string to names_set1.
'''
names_set1 = {'Dan'}
names_set2 = set()
names_set2.add(input())
names_set2.add(input())
names_set2.add(input())

names_set1.update(names_set2)
names_set1.remove(input())
names_set1.add(input())

print(f'names_set1: {sorted(names_set1)}')
print(f'names_set2: {sorted(names_set2)}')

'''
Level 4
Set my_favorites contains 14, 27, and 31. Set your_favorites contains three integers read from input. Assign numbers_not_shared with the set containing only elements that appear in exactly one of my_favorites and your_favorites.
'''
my_favorites = {14, 27, 31}
your_favorites = {int(input()), int(input()), int(input())}

numbers_not_shared = my_favorites.symmetric_difference(your_favorites)

print(f'My favorite numbers: {sorted(my_favorites)}')
print(f'Your favorite numbers: {sorted(your_favorites)}')
print(f'Numbers not shared: {sorted(numbers_not_shared)}')