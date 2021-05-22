class Rectangle:
    def __init__(self, wide=1, high=1):
        self.__width = wide
        self.__height = high

    def setWide(self, wide):
        self.__width = wide

    def setHigh(self, high):
        self.__height = high

    def getWide(self):
        return self.__width

    def getHigh(self):
        return self.__height

    def getArea(self):
        return (int(self.__width) * int(self.__height))

    def __str__(self):
        return("The width is: " + str(self.__width) + " "
        + "The height is: " + str(self.__height))

def main():
    x = Rectangle()
  
    x.setWide(input("Please enter a width value: "))
    x.setHigh(input("Please enter a height value: "))
    print("Width: ", x.getWide())
    print("Height: ", x.getHigh())

    print("Area: ", x.getArea())
    print("State: ", x)

main()