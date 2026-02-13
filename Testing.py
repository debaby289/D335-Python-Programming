color_dict = {
    'red': 0,
    'green': 0,
    'blue': 128
}

key_read = input()
value_read = input()

color_dict[key_read] = value_read

print(f'red: {color_dict["red"]}')
print(f'green: {color_dict["green"]}')
print(f'blue: {color_dict["blue"]}')
print(f'{key_read}: {color_dict[key_read]}')