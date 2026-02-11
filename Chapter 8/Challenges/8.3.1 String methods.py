'''
Challenge : String methods
Level 1
String string_of_letters is read from input. 
If "o" is in string_of_letters, then:

Output "At index: " followed by the index of the first occurrence.

Create a string from string_of_letters with the first three occurrences of "o" replaced by "(blank)" and output the new string on a new line.

Otherwise, output "No results".

Click here for example
Ex: If the input is ueeoaaiuooo, then the output is:
At index: 3
uee(blank)aaiu(blank)(blank)o
'''
string_of_letters = input()

if 'o' in string_of_letters:    #Search for 'o'
    first_index = string_of_letters.index('o')   #Find index of o
    print("At index:", first_index)   #Output

    # Replace 'o' with '(blank)'
    modified_string = string_of_letters.replace('o', '(blank)', 3)
    print(modified_string)   #Output the modified string
    
else:   #Second
    print('No results')      
'''
Level 2
Strings name1 and name2 are read from input. Write an if-else statement that compares the strings:

If name1 and name2 have exactly the same characters, output "Same inputs".
Otherwise, output the string with the greater ASCII value.
Click here for example

Ex: If the input is:
Ororo Munroe
Clark Kent

then the output is:
Ororo Munroe
'''
name1 = input()
name2 = input()

if name1 == name2:
    print('Same inputs')
elif name1 > name2:
    print(name1)
else:
    print(name2)  

'''
Level 3
String my_string is read from input.

If all the characters in my_string are numbers, then output "All numbers".

Otherwise, if all the characters in my_string are lowercase, then output "All lowercase".

If none of the above are true, output "No condition fits".
Click here for examples

Ex 1: If the input is 1236, then the output is:
All numbers
Ex 2: If the input is qkdvet, then the output is:
All lowercase
Ex 3: If the input is f9LFoO, then the output is:
No condition fits
'''
my_string = input()

if my_string.isdigit() == True:
    print('All numbers')
elif my_string.islower() == True:
    print('All lowercase')
else:
    print('No condition fits')

'''
Level 4
String color_string is read from input with leading and trailing whitespaces. 

Remove any leading and trailing whitespaces in the string. 

If color_string contains the string "Paint color:", capitalize the first letter for each word in color_string. 

Otherwise, capitalize all the characters in color_string. 
Finally, print out the resulting string.

Click here for examples
Ex 1: If the input is:
Paint color: teal 
then the output is:
Paint Color: Teal

Ex 2: If the input is:
red 
then the output is:
RED
'''
color_string = input()

color_string = color_string.strip()

if color_string.startswith('Paint color:'):
    print(color_string.title())
else: 
    print(color_string.upper())