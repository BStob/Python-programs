class Students(object):
    def __init__(self, fname="", lname="", mark=0):
        self.__first_name = fname
        self.__last_name = lname
        self.__mark = mark

    def setFirstName(self, fname):
        self.__first_name = fname

    def setLastName(self, lname):
        self.__last_name = lname

    def setMark(self, mark):
        self.__mark = mark

    def getMark(self):
        return (self.__mark)
    
    def __str__(self):
        return self.__first_name + " " + \
               self.__last_name + "\t" + \
               self.calcGrade()

class L7Student(Students):
    def calcGrade(self):
        if self.getMark() < 0 or self.getMark() > 100:
            print("Invalid Mark")
            return ""
        elif self.getMark() < 40:
            return  "Fail"
        elif self.getMark() < 50:
            return  "Pass"
        elif self.getMark() < 60:
            return  "Lower Merit"
        elif self.getMark() < 70:
            return  "Upper Merit"
        else:
            return "Distinction"

class L8Student(Students):
    def calcGrade(self):
        if self.getMark() < 0 or self.getMark() > 100:
            print("Invalid Mark")
            return ""
        elif self.getMark() < 40:
            return  "Fail"
        elif self.getMark() < 50:
            return  "Pass"
        elif self.getMark() < 60:
            return  "Second Grade Honours Grade 2"
        elif self.getMark() < 70:
            return  "First Grade Honours Grade 1"
        else:
            return "First Class Honours"


