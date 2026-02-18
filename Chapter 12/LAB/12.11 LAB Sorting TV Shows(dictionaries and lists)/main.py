'''
Docstring for Chapter 12.LAB.12.11 LAB Sorting TV Shows(dictionaries and lists).main
Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method. The input file contains an unsorted list of number of seasons followed by the corresponding TV show. Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, and a Python list of TV shows are the values (since multiple shows could have the same number of seasons).

Sort the dictionary by key (greatest to least) and output the results to a file named output_keys.txt. Separate multiple TV shows associated with the same key with a semicolon (;), ordering by appearance in the input file. Next, sort the dictionary by values (in reverse alphabetical order), and output the results to a file named output_titles.txt.

Ex: If the input is:
file1.txt

and the contents of file1.txt are:
20
Gunsmoke
30
The Simpsons
10
Will & Grace
14
Dallas
20
Law & Order
12
Murder, She Wrote

the file output_keys.txt should contain:
30: The Simpsons
20: Gunsmoke; Law & Order
14: Dallas
12: Murder, She Wrote
10: Will & Grace

and the file output_titles.txt should contain:
Will & Grace
The Simpsons
Murder, She Wrote
Law & Order
Gunsmoke
Dallas
'''
filename = input()

with open(filename, 'r') as f:
    lines = f.readlines()

# Build dictionary
tv_dict = {}
i = 0
while i < len(lines):
    seasons = int(lines[i].strip())
    show = lines[i + 1].strip()
    
    if seasons in tv_dict:
        tv_dict[seasons].append(show)
    else:
        tv_dict[seasons] = [show]
    i += 2

# Sort by keys (greatest to least) and write to output_keys.txt
with open('output_keys.txt', 'w') as f:
    for key in sorted(tv_dict.keys(), reverse=True):
        shows = '; '.join(tv_dict[key])
        f.write(f'{key}: {shows}\n')

# Sort by values (reverse alphabetical) and write to output_titles.txt
all_shows = []
for shows in tv_dict.values():
    for show in shows:
        all_shows.append(show)

all_shows_sorted = sorted(all_shows, reverse=True)

with open('output_titles.txt', 'w') as f:
    for show in all_shows_sorted:
        f.write(f'{show}\n')