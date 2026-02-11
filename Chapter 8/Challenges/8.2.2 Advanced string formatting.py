'''
Challenge : Advanced string formatting
Level 1
String food_name and integer food_quantity are read from input. Use one print(f' ') statement to output the following, all on one line:

food_name with a width of 16 characters, right-aligned, and with the fill character '('
food_quantity with a width of 16 characters, centered, and with the fill character ')'
Click here for example
Ex: If the input is:
yam
957

then the output is:
(((((((((((((yam))))))957)))))))
'''
food_name = input()
food_quantity = int(input())

print(f'{food_name:(>16}{food_quantity:)^16}')

'''
Level 2
Floating-point number inches_length is read from input. Then, inches_length is converted to feet and stored into variable feet_length. Use one print(f' ') statement to output 'After formatting: ', followed by feet_length to 6 decimal places and ' feet'.

Click here for example
Ex: If the input is 60.0, then the output is:
Before formatting: 5.0 feet
After formatting: 5.000000 feet
'''
inches_length = float(input())
feet_length = inches_length / 12

print(f'Before formatting: {feet_length} feet')
print(f'After formatting: {feet_length:.6f} feet')

'''
Level 3
Three strings are read from input and stored into list plants. Then, three more strings are read from input and stored into list colors. Lastly, string separator_char is read from input. Use five print(f' ') statements to output the following five lines:
    "Plants", with a field width of 26, centered. Then "Colors", with a field width of 26, centered.

    52 instances of separator_char.

    plants[0], with a field width of 26, left-aligned. Then, colors[0] with a field width of 26, left-aligned.

    plants[1], with a field width of 26, left-aligned. Then, colors[1] with a field width of 26, left-aligned.

    plants[2], with a field width of 26, left-aligned. Then, colors[2] with a field width of 26, left-aligned.
Click here for example
Ex: If the input is:
lilac peony maple
orange white purple
_

then the output is:

          Plants                    Colors          
____________________________________________________
lilac                     orange                    
peony                     white                     
maple                     purple    
'''
plants = input().split()
colors = input().split()
separator_char = input()

print(f'{"Plants":^26}{"Colors":^26}')
print(f'{separator_char}' * 52)
print(f'{plants[0]:<26}{colors[0]:<26}')
print(f'{plants[1]:<26}{colors[1]:<26}')
print(f'{plants[2]:<26}{colors[2]:<26}')
