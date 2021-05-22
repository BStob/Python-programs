def getPort():
    x = int(input("Please enter a TCP port number: "))
    return x
def isValidPort(x):
    if x >= 1 and x <= 1023:
        return "True"
    else:
        print("Invalid Port Number")
        return "False"
def displayPort(x):
    print("The entered port number was:", x)

def main():
    validCheck = "False"
    while validCheck != "True":
        portNum = getPort()
        validCheck = isValidPort(portNum)

    displayPort(portNum)
    return
main()
