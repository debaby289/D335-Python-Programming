'''
Challenge : Class and instance object types
Level 1
Define a class attribute named ft_to_inch in the Length class, and assign ft_to_inch with 12.

Ex: If the input is 33, then the output is:
33 feet = 396 inches
'''
class Length:
    ft_to_inch = 12

    def __init__(self):
        self.ft = 0
        
    def print_value(self):
        inch = self.ft * self.ft_to_inch
        print(f'{self.ft} feet = {inch} inches')

cord_length = Length()
cord_length.ft = int(input())
cord_length.print_value()

'''
Level 2
In the print_value() method of the Time class object:

If the class attribute show_in_s is True, then output 'Time in seconds: ' followed by instance attribute value_in_m multiplied by 60.
Otherwise, output 'Time in minutes: ' followed by the value of instance attribute value_in_m.

Click here for example
Ex: If the input is:
36
43

then the output is:
First time measurement:
Time in seconds: 2160
Second time measurement:
Time in minutes: 43
'''
class Time:
    show_in_s = True
      
    def __init__(self):
        self.value_in_m = 0
  
    def print_value(self):
        if self.show_in_s == True:
            print(f'Time in seconds: {self.value_in_m * 60}')
        else:
            print(f'Time in minutes: {self.value_in_m}')
  
record_time1 = Time()
record_time1.value_in_m = int(input())
print('First time measurement:')
record_time1.print_value()

Time.show_in_s = False

record_time2 = Time()
record_time2.value_in_m = int(input())
print('Second time measurement:')
record_time2.print_value()

'''
Level 3
In method cook() of the StrawberryPie class, perform the following tasks:
    Increment class attribute total_pies.
    Assign instance attribute num_strawberries with the value of parameter strawberries_used.
    Output 'One strawberry pie made with ', followed by the value of instance attribute num_strawberries, and ' strawberries'.

Click here for example
Ex: If the input is 4 10 8, then the output is:
One strawberry pie made with 4 strawberries
One strawberry pie made with 10 strawberries
One strawberry pie made with 8 strawberries
Number of strawberry pies made: 3
Total number of strawberries used: 22

Note: StrawberryPie.total_pies should be used when modifying class attribute total_pies.
'''
class StrawberryPie:
    total_pies = 0
    
    def __init__(self):
        self.num_strawberries = 0

    def cook(self, strawberries_used):
        StrawberryPie.total_pies += 1
        self.num_strawberries += strawberries_used
        num_strawberries = strawberries_used
        print(f'One strawberry pie made with {num_strawberries} strawberries')
    
total_strawberries_used = 0
for token in input().split():
    strawberry_pie = StrawberryPie()
    strawberry_pie.cook(int(token))
    total_strawberries_used += strawberry_pie.num_strawberries
print(f'Number of strawberry pies made: {StrawberryPie.total_pies}')
print(f'Total number of strawberries used: {total_strawberries_used}')
