'''
Task:
Write a Python program that performs the following steps:
    Prompt the user to input the name of a CSV file ("input1.csv").
    Use Python's built-in csv module to open and read the specified file.
    For each row in the file, reverse the order of elements (values separated by commas).
    Print the reversed elements for each row to the console.

Requirements:
    Use the open() function to open the file.
    Use the csv.reader() method to read the file contents.
    Use a loop to iterate through each row and reverse the elements in the row.
    Print the reversed elements as a list for each row.

Sample Input and Output:
If the input is
Enter the name of the file along with its extension:
input1.csv  

Contents of input1.csv:
    fruits,sports,countries
    banana,football,United States
    apple,soccer,Brazil
    orange,volleyball,Canada

Then the expected output is
    ['countries', 'sports', 'fruits']  
    ['United States', 'football', 'banana']  
    ['Brazil', 'soccer', 'apple']  
    ['Canada', 'volleyball', 'orange'] 
Hints: Use Python's [::-1] slicing technique to reverse a list.
'''
import csv

# accept string input identifying filename
print("Enter the name of the file along with its extension:")
file_name = input()

# open, read, and output rows in reverse order
with open(file_name, 'r') as csvfile:
    reader = csv.reader(csvfile)
    
    for row in reader:
        reversed_row = row[::-1]   # reverse the row
        print(reversed_row)