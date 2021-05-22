from shapes import Circle 

def main():
    object1 = Circle()
    object2 = Circle(20)

    print(object1)
    print(object2)

    object1.setRad(10)
    print(object1)


main()