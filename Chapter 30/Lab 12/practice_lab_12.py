'''
Task:
Write a Python program that performs the following steps:
Prompt the user to input the name of a text file (e.g., "WordTextFile.txt").
The input file contains exactly three rows, each containing a single word.
Using the open() function and the read() and write()methods, perform the following actions:
    Read the three words from the file.
    Construct a new sentence by combining these words in the same order, separating the words by spaces.
    Append this sentence to the end of the file on a new line.
Display the updated contents of the file.

Requirements:
    Use the open() function in the appropriate mode to read and write to the file.
    Ensure the words in the sentence are separated by a single space.
    Output the complete updated contents of the file, showing the original words followed by the newly appended sentence.

Output Format:
The program should print the updated file contents, with the original words on separate lines and the new sentence on a new line.

Sample Input and Output:
If the input is
Enter the name of the input file:
WordTextFile.txt
Contents of WordTextFile.txt before the program runs:
    cat  
    chases  
    dog  
then the expected output is
    cat  
    chases  
    dog  
    cat chases dog  
'''
print("Enter the name of the input file:")
filename = input()

# 🔹 Step 1: Read the words
file = open(filename, 'r')
content = file.read()
file.close()

# Split into lines (words)
words = content.strip().split('\n')

# 🔹 Step 2: Build the sentence
sentence = ' '.join(words)

# 🔹 Step 3: Append sentence to file
file = open(filename, 'a')
file.write('\n' + sentence)
file.close()

# 🔹 Step 4: Display updated contents
file = open(filename, 'r')
updated_content = file.read()
file.close()

print(updated_content)