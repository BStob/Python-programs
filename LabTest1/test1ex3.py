def main():
    x = getCC()
    helloTest(x)
    

def getCC():
    x = input("Please enter your current course codes: ")
    return x

def helloTest(x):
    y = booleanCheck(x)
    if y == 'True':
        print("Welcome to SOFT2022!")
    else:
        print("Not taking the SOFT2022 module")

def booleanCheck(x):
    if ("SOFT2022" in x) == True:
        return 'True'
    else:
        return 'False'
main()
