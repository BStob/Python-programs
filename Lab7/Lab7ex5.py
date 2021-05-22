def main():
    marks = open("marks.txt", "r")
    count = marks.readline()
    z = 0
    while count:
        if int(count) > int(z):
            z = count
        count = marks.readline()
    print("The highest mark was: ", z)     
    marks.close()

main()
