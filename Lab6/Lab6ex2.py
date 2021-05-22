def main():
    i = 0
    list1 = []
    list1 = getInput()
    for i in list1:
        print(i, end = " ")
    
    print("\n", id(list1))
    cubeList(list1)
    
    
    
    
def getInput():
    i = 0
    x = []
    for i in range(10):
        y = float(input("Please enter a Variable: "))
        x.append(y)
    return x

def cubeList(x):
    i = 0
    for i in range(len(x)):
        x[i] = x[i]**3
    for i in x:
        print(i, end = " ")
    
    print("\n", id(x))
    
    
main()
