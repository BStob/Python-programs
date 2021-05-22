#Ben Stobie
#16/04/21

class Student:
    def __init__(self, fname, lname):
        self.first_name = fname 
        self.last_name = lname 


def main():
    studentName1 = Student(input("Please enter your first name: "), input("Please enter your last name: "))
    studentName2 = Student(input("Please enter your partner's first name: "), input("Please enter your partner's last name: "))
    studentName3 = Student(input("Please enter your partner's first name: "), input("Please enter your partner's last name: "))
    print(studentName1.first_name, end = " ")
    print(studentName1.last_name)
    print(studentName2.first_name, end = " ")
    print(studentName2.last_name)
    print(studentName3.first_name, end = " ")
    print(studentName3.last_name)
main()