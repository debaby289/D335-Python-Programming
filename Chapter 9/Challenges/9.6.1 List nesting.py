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
Integer num_salads is read from input, representing the number of rows of data remaining in the input. Two-dimensional list ingredient_lists consists of data read from the remaining input, with each row representing the ingredients of a fruit salad. For each row of ingredient_lists:
    Output 'Ingredients in salad ', the row index plus 1, and ':' on one line.
    Output all the elements in the row on the next line, ending each element with a space.

Click here for example
Ex: If the input is:
3
cherry berry lemon
peach pineapple
mango quince grape apple

then the output is:
Ingredients in salad 1:
cherry berry lemon 
Ingredients in salad 2:
peach pineapple 
Ingredients in salad 3:
mango quince grape apple 

Note:
    enumerate() returns the index and the value of the list element in the current iteration.
    print(x, end=' ') outputs x and ends with a space instead of a default newline.
'''

'''
Level 4

'''
