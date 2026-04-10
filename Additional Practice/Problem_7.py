'''
Write a program that:
    Asks the user for a filename
    Asks the user to enter names until they type "done"
    Writes all names to the file (one per line)
    Then reads the file back and prints:
        Total number of names
        All names in alphabetical order

Expected behavior:
    Enter filename: names.txt
    Enter name (or 'done' to finish): Alice
    Enter name (or 'done' to finish): Charlie
    Enter name (or 'done' to finish): Bob
    Enter name (or 'done' to finish): done

    Names written to names.txt

    Total names: 3
        Names in alphabetical order:
        Alice
        Bob
        Charlie
'''
user_file = input('Enter filename: ')

with open(f'{user_file}','w') as f:
    names = input('Enter name (or \'done\' to finish):')
    while names != 'done':
        f.write(f'{names}\n')
        names = input('Enter name (or \'done\' to finish):')

print(f'\nNames written to {user_file}')

with open(user_file, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

print(f'\nTotal names: {len(lines)}')
print('Names in alphabetical order:')
for name in sorted(lines):
    print(f'{name}')