'''
Challenge : Detect specific values
Level 1
If dimensions_number is 3, output 'Three-dimensional space'. Otherwise, output 'Not a three-dimensional space'.
'''
dimensions_number = int(input())

if dimensions_number == 3:
    print('Three-dimensional space')
else:
    print('Not a three-dimensional space')

'''
Level 2
If num_players is:
    2, output 'Duo'.
    4, output 'Quartet'.

Otherwise, output 'Other number of musicians'.
'''
num_players = int(input())

if num_players == 2:
    print('Duo')
elif num_players == 4:
    print('Quartet')
else:
    print('Other number of musicians')

'''
Level 3
If num_parts is:
    1, output 'Monad'.
    2, output 'Dyad'.
    3, output 'Triad'.
Otherwise, output 'Other number of parts'.
'''
num_parts = int(input())

if num_parts == 1:
    print('Monad')
elif num_parts == 2:
    print('Dyad')
elif num_parts == 3:
    print('Triad')
else:
    print('Other number of parts')