'''
Docstring for Chapter 5.Challenges.5.12.3 Conditional expression Conditional assignment
Using a conditional expression, write a statement that increments num_users if update_direction is 3, otherwise decrements num_users.
'''
num_users = int(input())
update_direction = int(input())

num_users = num_users + 1 if update_direction == 3 else num_users - 1

print(f'New value is: {num_users}')