#Ben Stobie
#26 March 2021

def main():
    students = {}
    i = 0
    while i != 5:
        stdInfo = []
        stdID = input("Please enter the student's ID number: ")
        while stdID in students:
            print("Input failed")
            stdID = input("Please enter another student's ID number: ")
        stdInfo.append(input("Please enter the student's name: "))
        stdInfo.append(input("Please enter the Course name: "))
        stdInfo.append(int(input("Please enter the Student's Mark: ")))
        students[stdID] = stdInfo
        i = i+1
    for x in students:
        print("Name: ", students[x][0])
        print("Course: ", students[x][1])
        print("Mark: ", students[x][2])
        print(" ")

main()
