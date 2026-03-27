'''
Task:
Create a solution that accepts three integer inputs representing the number of times an employee travels to a job site in a month. Output the total distance traveled to two decimal places according to the miles each employee commutes to the job site:
    Employee A: 15.62 miles
    Employee B: 41.85 miles
    Employee C: 32.67 miles
The solution output should be in the format:
    Distance: total_miles_traveled miles

Sample Input/Output:
If the input is
    3
    10
    5
then the expected output is
    Distance: 628.71 miles
'''
#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#solution accepts three integer inputs representing the number of times an employee travels to the job site
#solution outputs "Distance: " followed by the total value to two decimal places

#accept three integer inputs
print("Enter the number of days Employee A travels to job:")
Employee_A = int(input())
print("Enter the number of days Employee B travels to job:")
Employee_B = int(input())
print("Enter the number of days Employee C travels to job:")
Employee_C = int(input())

#calculate total distance
a_miles = 15.62
b_miles = 41.85
c_miles = 32.67

#output combined mileage
total_distance = (Employee_A * a_miles) + (Employee_B * b_miles) + (Employee_C * c_miles)
print(f'Distance: {total_distance:.2f} miles')