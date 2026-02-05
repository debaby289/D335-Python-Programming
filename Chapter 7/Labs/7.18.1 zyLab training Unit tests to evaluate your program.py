'''
Docstring for Chapter 7.Labs.7.18.1 zyLab training Unit tests to evaluate your program
The program defines the following function: def kilo_to_pounds(kilos)that takes kilos as a parameter, converts kilos from kilograms to pounds, and returns the weight in pounds. This lab uses multiple unit tests to test kilo_to_pounds(). 

The program takes a weight in kilograms as input, converts the weight to pounds, and then outputs the weight in pounds, where 1 kilogram = 2.204 pounds (lbs). 

Ex: If the input of the program is:
10

10 is passed to kilo_to_pounds() and the output of the program is:
22.040 lbs

The program below has two errors.
(1) Click the Run button. Notice that your code runs and given an input is provided, an output is produced in the console. 

(2) Now click the Submit for grading button. Notice the last two test cases fail with an error message ending with ImportError: cannot import name "kilo_to_pounds" from "main" (/usercode/main.py). 

This issue occurred because the function name was mistyped with the incorrect capitalization. Function names are case-sensitive, so if a lab program expects a kilo_to_pounds() function, using kilo_To_Pounds() will still cause the unit test to fail. The unit test will not recognize kilo_to_pounds() because the exact case-sensitive match is missing. However, the program runs in the console because the function being called in main has the same name, with the exact case match, as the function defined.

(3) Update the function name to kilo_to_pounds() and submit for grading. Notice that the first two test cases fail, but the third test case passes. 
The first test case fails because the program outputs an incorrect value from the kilo_to_pounds() function. 
The second test case uses a Unit test to test the kilo_to_pounds() function and fails because kilo_to_pounds() returned an incorrect value.

(4) Change the kilo_to_pounds() function to multiply the variable kilos by 2.204, instead of dividing. The return statement should be: return (kilos * 2.204). Run the program to verify that the correct output is produced. Submit for grading again and confirm all test cases pass.
'''
def kilo_to_pounds(kilos):
    # This statement intentionally has an error.
    return (kilos * 2.204)


# Main part of the program starts here. Do not remove the line below.
if __name__ == "__main__":
    kilos = float(input())

    pounds = kilo_to_pounds(kilos)
    print(f"{pounds:.3f} lbs")
