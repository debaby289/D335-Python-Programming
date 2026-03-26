'''
Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method. The file contains a list of words separated by commas. The program must output the words and their frequencies (the number of times each word appears in the file) without any duplicates.

Ex: If the input is:
    input1.csv

and the contents of input1.csv are:
    hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy

the output is:
    hello - 1
    cat - 2
    man - 2
    hey - 2
    dog - 2
    boy - 2
    Hello - 1
    woman - 1
    Cat - 1

Notes: Output words in order of first occurrence in input and end output with a newline. File input1.csv is available to download.
'''
import csv

# Type your code here. 
file = input()

word_count = {}

with open(f'{file}','r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        # row is a list of words from one row of CSV
        for word in row:
            # Count this word
            if word not in word_count:
                # First occurrence
                word_count[word] = 1
            else:
                # Seen before
                word_count[word] += 1

# Output results
for word, count in word_count.items():
    print(f'{word} - {count}')