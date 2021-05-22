#Ben Stobie
#16/04/21

class Student:
    def __init__(self, fname, lname, age):
        self.__first_name = fname 
        self.__last_name = lname 
        self.__student_age = age
    
    def __str__(self): 
        return (self.__first_name + " " + self.__last_name + " " + self.__student_age)


def main():
    studentName = str(Student(input("Please enter your first name: "), input("Please enter your last name: "), input("Please enter your age: ")))
    print(studentName)
main()