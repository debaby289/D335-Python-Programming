'''
Step 0: Read the template file and do not change the provided code. 
The program reads a symbol and the triangle's height from a user and outputs a fixed-hight right triangle using * characters.

Step 1 (1 pt): Output the same right triangle with user-specified characters. 
Modify the program to output the same right triangle using the user-specified triangle_char characters instead of *. Submit for grading to confirm 1 test passes.

Ex: If triangle_char = % and triangle_height = 5, the output is:

Enter a character:
    %
Enter triangle height:
    5

% 
% % 
% % % 

Step 2 (2 pts): Output a right triangle with user-specified characters and height. 
Modify the program to use a nested loop to output a right triangle of height triangle_height. The first line will have one user-specified character. Each subsequent line will have one additional user-specified character until the number in the triangle's base reaches triangle_height. Output a space after each user-specified character, including after the line's last user-specified character. Submit for grading to confirm all tests pass.

Ex: If triangle_char = % and triangle_height = 5, the output is:
Enter a character:
    %
Enter triangle height:
    5

% 
% % 
% % % 
% % % % 
% % % % % 
'''
triangle_char = input("Enter a character:\n")
triangle_height = int(input("Enter triangle height:\n"))
print("")

for i in range(1, triangle_height + 1):
    for j in range(i):
        print(triangle_char, end=" ")
    print()