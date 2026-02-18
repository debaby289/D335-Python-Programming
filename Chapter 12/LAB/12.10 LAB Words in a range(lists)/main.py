'''
Docstring for Chapter 12.LAB.12.10 LAB Words in a range(lists).main
Write a program that first reads in the name of an input file, followed by two strings representing the lower and upper bounds of a search range. The file should be read using the file.readlines() method. The input file contains a list of alphabetical, ten-letter strings, each on a separate line. Your program should determine if the strings from the list are within that range (inclusive of the bounds) and output the results.

Ex: If the input is:
input1.txt
ammoniated
millennium

and the contents of input1.txt are:
aspiration
classified
federation
graduation
millennium
philosophy
quadratics
transcript
wilderness
zoologists

the output is:
aspiration - in range
classified - in range
federation - in range
graduation - in range
millennium - in range
philosophy - not in range
quadratics - not in range
transcript - not in range
wilderness - not in range
zoologists - not in range
'''
filename = input()
lower_bound = input()
upper_bound = input()

with open(filename, 'r') as f:
    words = f.readlines()

for word in words:
    word = word.strip()  # Remove newline character
    if lower_bound <= word <= upper_bound:
        print(f'{word} - in range')
    else:
        print(f'{word} - not in range')