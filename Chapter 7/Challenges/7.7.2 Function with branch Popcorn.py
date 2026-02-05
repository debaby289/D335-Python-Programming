'''
Docstring for Chapter 7.Challenges.7.7.2 Function with branch Popcorn
Define function print_popcorn_time() with parameter bag_ounces. If bag_ounces is less than 3, print "Too small". If greater than 10, print "Too large". Otherwise, compute and print 6 * bag_ounces followed by " seconds".

Sample output with input: 7
42 seconds
'''
#Function def
def print_popcorn_time(bags):
    #Conditonals
    if bags < 3:
        print('Too small')
    elif bags > 10:
        print('Too large')
    else:
        print(f'{6 * bags} seconds')

bag_ounces = int(input())
print_popcorn_time(bag_ounces)