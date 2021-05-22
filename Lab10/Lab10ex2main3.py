from rectangle import Rectangle

def main():
    object1 = Rectangle(input("Wide: "), input("High: "))

    print(object1)

    print("Area: " + str(object1.getArea()))


main()