'''
Define a Course base class with the following attributes:
    number - course number
    title - course title
    Define a print_info() method in Course that displays the course number and title.

Also define a derived class OfferedCourse with the additional attributes:
    instructor_name - instructor name
    location - class location
    class_time - class time

Ex: If the input is:
    ECE287
    Digital Systems Design
    ECE387
    Embedded Systems Design
    Mark Patterson
    Wilson Hall 231
    WF: 2-3:30 pm

the output is:
    Course Information:
    Course Number: ECE287
    Course Title: Digital Systems Design
    Course Information:
    Course Number: ECE387
    Course Title: Embedded Systems Design
    Instructor Name: Mark Patterson
    Location: Wilson Hall 231
    Class Time: WF: 2-3:30 pm
'''
class Course:
    def __init__(self, number, title):
        self.number = number
        self.title = title
    
    def print_info(self):
        print('Course Information:')
        print(f'   Course Number: {self.number}')
        print(f'   Course Title: {self.title}')


class OfferedCourse(Course):
    def __init__(self, number, title, instructor_name, location, class_time):
        Course.__init__(self, number, title)
        self.instructor_name = instructor_name
        self.location = location
        self.class_time = class_time


if __name__ == "__main__":
    course_number = input()
    course_title = input()

    o_course_number =  input()
    o_course_title =  input()
    instructor_name = input()
    location = input()
    class_time = input()
    
    my_course = Course(course_number, course_title)
    my_course.print_info()
    
    my_offered_course = OfferedCourse(o_course_number, o_course_title, instructor_name, location, class_time)
    my_offered_course.print_info()

    print(f'   Instructor Name: { my_offered_course.instructor_name }')
    print(f'   Location: { my_offered_course.location }')
    print(f'   Class Time: { my_offered_course.class_time }')