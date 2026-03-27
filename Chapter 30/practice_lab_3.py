'''
Task:
Create a solution that accepts an integer input representing the index value for any of the seven elements in the following list:
    data_mixture = ["Python is fun", 2024, 5.67, ["apple", "banana", "coconut"], None,{"name": "John", "age": 25}]

The solution should perform the following:
    Retrieve the element at the given index.
    Determine its data type using the type() function and its .name attribute.
    Check if the element belongs to one of the following categories:
        If the element is "iterable" (e.g., list, str, dict), output, "This element is iterable."
        If the element is numeric (e.g., int, float), output, "This element is numeric."
    For other data types not in these categories, output, "This is a different data type."

The solution output should be in the format:
    Element: [element_value], Type: [data_type], Message: [category_message]

Sample Input and Output:
If the input is
    Enter index:
    3
then the expected out is
    Element: ['apple', 'banana', 'coconut'], Type: list, Message: This element is iterable.

Alternatively, if the input is
    Enter index:
    1
then the expected output is
    Element: 2024, Type: int, Message: This element is numeric.
'''
#list of mixed data elements
data_mixture = ["Python is fun", 2024, 5.67, ["apple", "banana", "coconut"], None, {"name": "John", "age": 25}]

#input for index
print("Enter index:")
index = int(input())

#retrieve elements
element = data_mixture[index]

element_type = type(element).__name__

if element_type in ('list','str','dict'):
    message = 'This element is iterable.'
else:
     message = 'This element is numeric.'

print(f'Element: {element}, Type: {element_type}, Message: {message}')

