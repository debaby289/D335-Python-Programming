'''
Docstring for Chapter 9.Labs.9.22 LAB Contact list
A contact list is a place where you can store a specific contact with other associated information such as a phone number, email address, birthday, etc. 

Write a program that first takes in word pairs that consist of a name and a phone number (both strings), separated by a comma.
That list is followed by a name, and your program should output the phone number associated with that name. 
Assume the search name is always in the list.

Ex: If the input is:
Joe,123-5432 Linda,983-4123 Frank,867-5309
Frank
the output is:
867-5309
'''

contact_info = input()

contact_dict = {}
for contact in contact_info.split():
    key_read,value_read = contact.split(',')
    contact_dict[key_read] = value_read

search_name = input()
print(f'{contact_dict[search_name]}')