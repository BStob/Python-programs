import rectangle as rect

def main():
    object1 = rect.Rectangle(input("Wide: "), input("High: "))

    print(object1)

    print("Area: " + str(object1.getArea()))


main()