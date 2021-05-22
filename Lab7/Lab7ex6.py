def main():
    student = open("students.txt", "r")
    readData = student.readline()
    readData = student.readline()
    y = 0
    while readData:
        splitData = readData.split(",")
        x = splitData[2]
        if int(x) > int(y):
            a = splitData[0]
            b = splitData[1]
            y = splitData[2]
        readData = student.readline()
    print("Student Name: ", a)
    print("Subject: ", b)
    print("Mark: ", y)


main()
