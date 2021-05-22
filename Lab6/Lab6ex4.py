def main():
    list1 = getList()
    sortList(list1)
    sliceList(list1)

def getList():
    i = 0
    y = []
    x = input("Please enter a sentence (min 6 words): ")
    y = x.split()
        
    while (len(y)) < 6:
        print("Invalid Input \n")
        x = input("Please enter a sentence (min 6 words): ")
        y = x.split()
    if "ip" or "IP" in y:
        print("IP detected in list \n")
    return y

def sortList(x):
    i = 0
    x.sort()
    for i in x:
        print(i, end = " ")
    print("\n")

def sliceList(x):
    y = x[0:2]
    for i in y:
        print(i, end = " ")
main()
