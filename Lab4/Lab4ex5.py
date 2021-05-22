def main():
    width = getWidth()
    height = getHeight()

    
    doLine(width)
    doSides(width, height)
    doLine(width)
     
    return

def getWidth():
    x = int(input("Input the width of the rectangle: "))
    return x

def getHeight():
    x = int(input("Input the height of the rectangle: "))
    return x

def doLine(x):
    i = 0
    while i <= x:
        print("#", end = " ")
        i = i + 1

def doSides(x, y):
    space = int(x) - 2
    high = int(y) - 2
    i = 0
    f = 0

    while f <= high:
        print(" ")
        print("#", end = " ")
        while i <= space:
            print(" ", end = " ")
            i = i + 1
        print("#")
        f = f + 1
        i = 0
    return
main()
    
