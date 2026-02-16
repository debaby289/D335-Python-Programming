'''
Docstring for Chapter 11.Challenges.11.1.2 Modules.Level 3.main
Perform the following tasks:
    Assign has_clothing with the value returned by search's find() called with one_sentence and clothing's search_list as the arguments, respectively.
    Assign has_person_and_color with the value returned by combining the following, using logical AND:
        search's find() called with one_sentence and persons's search_list as the arguments, respectively.
        search's find() called with one_sentence and colors's search_list as the arguments, respectively.

Click here for example
Ex: If the input is She bought a red sweater., then the output is:
The sentence mentions a piece of clothing.
The sentence mentions a person and a color.
'''
import persons
import colors
import clothing
import search

one_sentence = input()

has_clothing = search.find(one_sentence, clothing.search_list)

has_person_and_color = search.find(one_sentence, persons.search_list) and search.find(one_sentence, colors.search_list)

if has_clothing:
	print('The sentence mentions a piece of clothing.')

if has_person_and_color:
	print('The sentence mentions a person and a color.')