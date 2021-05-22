import rectangle 

def main():
    object1 = rectangle.Rectangle(input("Wide: "), input("High: "))

    print(object1)

    print("Area: " + str(object1.getArea()))


main()