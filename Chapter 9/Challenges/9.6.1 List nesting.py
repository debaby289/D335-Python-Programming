'''
Challenge : 
Level 1
Lists word1 and word2 are read from input. Assign all_words with a two-dimensional list consisting of word1 and word2 in that order.

Click here for example
Ex: If the input is:
t e a
c o f f e e
then the output is:
['t', 'e', 'a']
['c', 'o', 'f', 'f', 'e', 'e']
'''
word1 = input().split()
word2 = input().split()

all_words = word1,word2
print(all_words)

print(all_words[0])
print(all_words[1])

'''
Level 2
Two-dimensional list game_board represents a 3x3 tic-tac-toe game board read from input. List game_board contains three lists, each representing a row. Each list has three elements representing the three columns on the board. Each element in the tic-tac-toe game board is 'x', 'o', or '-'.

If all the elements at column index 0 are 'o', output 'Player o wins at column 0.' Otherwise, output 'Player o does not win at column 0.'

Click here for examples
Ex 1 (win): If the input is:
o - x
o - -
o - x
then the output is:
Player o wins at column 0.

Ex 2 (lose): If the input is:
x o x
o - -
o - -
then the output is:
Player o does not win at column 0.

Note: The logical test (a == 'o' and b == 'o' and c == 'o') returns True if a, b, and c are equal to 'o'. The logical test returns False otherwise.
'''
game_board = [
  input().split(),
  input().split(),
  input().split()
]

if game_board[0][0] == 'o':
    if game_board[1][0] == 'o':
        if game_board[2][0] == 'o':
            print(f'Player o wins at column 0.')
else:
    print(f'Player o does not win at column 0.')

'''
Level 3
Integer num_lines is read from input, representing the number of rows of data remaining in the input. Two-dimensional list data_2d consists of data read from the remaining input. Output each row of numbers in data_2d on one line, ending each number with a space.

Click here for example
Ex: If the input is:
3
27 16 19
46 75
61 28 15 23
then the output is:
27 16 19 
46 75 
61 28 15 23 
'''
num_lines = int(input())
data_2d = []
for row_index in range(num_lines):
    row_elements = []
    for x in input().split():
        row_elements.append(int(x))
    data_2d.append(row_elements)

for row in data_2d:
    for element in row:
        print(element, end=' ')
    print()

'''
Level 4
Integer grid_size is read from input, representing the number of rows and columns of a two-dimensional list. Two-dimensional list pattern_grid is created with zeros, 0, as the initial values. For each element at row index m and column index n of pattern_grid, assign the element with the value of m minus n.

Click here for example
Ex: If the input is 3, then the output is:
0 -1 -2 
1 0 -1 
2 1 0 
'''
grid_size = int(input())

pattern_grid = []
for m in range(grid_size):
    row = []
    for n in range(grid_size):
        row.append(0)
    pattern_grid.append(row)

for m in range(grid_size):
    for n in range(grid_size):
        pattern_grid[m][n] = m - n

for row in pattern_grid:
    for cell in row:
        print(cell, end=' ')
    print()