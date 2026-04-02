'''
**Problem 3: String Manipulation**

Write a program that:
- Asks the user for a sentence
- Outputs:
  - The sentence in reverse
  - Number of vowels (a, e, i, o, u)
  - Number of words
  - The sentence in uppercase

**Expected output:**
```
Enter a sentence: Hello World
Reversed: dlroW olleH
Vowels: 3
Words: 2
Uppercase: HELLO WORLD
'''
user_sentence = input('Enter a sentence: ')

reversed_sentence = user_sentence[::-1]
print(f'Reversed: {reversed_sentence}')

num_words = len(user_sentence.split())
vowels = 0

for sen in user_sentence:
    if sen.lower() in ('a','e','i','o','u'):
        vowels += 1

print(f'Vowels: {vowels}')

print(f'Words: {num_words}')

upper_sen = user_sentence.upper()
print(f'Uppercase: {upper_sen}')