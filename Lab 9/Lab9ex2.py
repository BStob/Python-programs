#Ben Stobie
#16/04/21

class Student:
    def __init__(self, fname, lname, age):
        self.first_name = fname 
        self.last_name = lname 
        self.student_age = age


def main():
    studentName = Student(input("Please enter your first name: "), input("Please enter your last name: "), input("Please enter your age: "))
    print(studentName.first_name, end = " ")
    print(studentName.last_name)
    print(studentName.student_age)
main()