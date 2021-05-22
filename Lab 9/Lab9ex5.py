#Ben Stobie
#16/04/21

class Student:
    def __init__(self, fname, lname):
        self.__first_name = fname 
        self.__last_name = lname 
        self.__student_mark = []

    def set_first_name(self, fname):
        self.__first_name = fname

    def set_last_name(self, lname):
        self.__last_name = lname

    def add_mark(self, mark):
        self.__student_mark.append( mark )

    
    def __str__(self): 
        c = 0
        i = 0
        ranVar = "Name: " + self.__first_name + " " + self.__last_name + " Marks: "
        for c in self.__student_mark:
            ranVar = ranVar + "" + c 
            if i != 2:
                ranVar = ranVar + ", "
            i = i + 1
        return ranVar


def main():
    i = 0
    studentName = Student("", "")
    studentName.set_first_name(input("Enter your first name: "))
    studentName.set_last_name(input("Enter your last name: "))
    while i < 3:
        studentName.add_mark(input("Enter the various marks: "))
        i = i + 1

    print(studentName)
main()