'''
**Problem 4: List Operations**

Write a program that:
- Creates a list: `numbers = [12, 5, 8, 3, 19, 7, 15]`
- Prints all even numbers from the list
- Prints all numbers greater than 10
- Prints the sum of all numbers
- Adds the number 25 to the list and prints the updated list

**Expected output:**
```
Even numbers: [12, 8]
Numbers > 10: [12, 19, 15]
Sum: 69
Updated list: [12, 5, 8, 3, 19, 7, 15, 25]
'''
numbers = [12, 5, 8, 3, 19, 7, 15]

evens = []
odds = []
greater_than_10 = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)
    elif num % 2 != 0:
        odds.append(num)

    if num > 10:
        greater_than_10.append(num)

sum_amount = sum(numbers)

numbers.append(25)

print(f'Even numbers: {evens}')
print(f'Numbers > 10: {greater_than_10}')
print(f'Sum: {sum_amount}')
print(f'Updated list: {numbers}')