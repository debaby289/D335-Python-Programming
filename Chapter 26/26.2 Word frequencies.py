'''
Write a program that reads a list of words. Then, the program outputs those words and their frequencies (case insensitive).

Ex: If the input is:
    hey Hi Mark hi mark

the output is:
    hey 1
    Hi 2
    Mark 2
    hi 2
    mark 2

Hint: Use lower() to set each word to lowercase before comparing.
'''
words = input().split()

for word in words:
    count = 0
    for w in words:
        if word.lower() == w.lower():
            count += 1
    print(f"{word} {count}")