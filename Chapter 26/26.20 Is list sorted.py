'''
Write a program that reads a list of integers from input and outputs "yes" if the list is sorted in ascending order between two provided positions. Otherwise, output "no". The first set of inputs is the list. The next two inputs are the start and end positions (inclusive). Assume position 1 is the first element of the list.

Ex: If the input is:
    5 6 7 4 3 2 1 0
    1 3
the output is:
    yes

Ex: If the input is:
    1 2 3 4 5 2
    4 6
the output is:
    no
'''
nums = list(map(int, input().split()))
start, end = map(int, input().split())

# Convert to 0-based indexing
start -= 1
end -= 1

is_sorted = True

for i in range(start, end):
    if nums[i] > nums[i + 1]:
        is_sorted = False
        break

print("yes" if is_sorted else "no")