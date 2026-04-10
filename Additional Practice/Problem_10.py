'''
Problem 10: Multi-Concept Integration (The Grand Finale!)
Write a program that:
    Asks the user for a filename containing integers (one per line)
    Reads the file
    Creates a dictionary with:
        Key: "even" → List of even numbers
        Key: "odd" → List of odd numbers
    Writes two output files:
        even_numbers.txt - all even numbers
        odd_numbers.txt - all odd numbers
    Prints summary statistics

Example:
Input file (numbers.txt):
    5
    10
    15
    20
    3
    8

Expected output:
Enter filename: numbers.txt
    Processing complete!
    Even numbers: 3 (written to even_numbers.txt)
    Odd numbers: 3 (written to odd_numbers.txt)
    Total numbers processed: 6

even_numbers.txt:
    10
    20
    8

odd_numbers.txt:
    5
    15
    3
'''
file_name = input('Enter filename: ')

numbers = {"even": [], "odd": []}

with open(file_name, 'r') as f:
    for line in f:
        num = int(line.strip())
        if num % 2 == 0:
            numbers["even"].append(num)
        else:
            numbers["odd"].append(num)

with open('even_numbers.txt', 'w') as e:
    for num in numbers["even"]:
        e.write(f"{num}\n")

with open('odd_numbers.txt', 'w') as o:
    for num in numbers["odd"]:
        o.write(f"{num}\n")

print('Processing complete!')
print(f'Even numbers: {len(numbers["even"])} (written to even_numbers.txt)')
print(f'Odd numbers: {len(numbers["odd"])} (written to odd_numbers.txt)')
print(f'Total numbers processed: {len(numbers["even"]) + len(numbers["odd"])}')