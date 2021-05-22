def userInput():
    x = int(input("Please enter a TCP port number: "))
    while x < 1 or x > 1023:
        x = int(input("Please enter a valid TCP port number (range 1 - 1023): "))

    return x

portNum = userInput()
print("The entered port number was: ", portNum)
