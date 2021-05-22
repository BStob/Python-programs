from random import randint

def main():
    list1 = []
    i = 0
    for i in range(30):
        list1.append(randint(0,100))
        print(list1[i - 1], end = " ")
        if i == 9 or i == 19 or i == 29:
            print("\n")
    minAndMax(list1)
    totalValue(list1)

def minAndMax(x):
    print("The max value of the list is: ", max(x))
    print("The minimum value of the list is: ", min(x))

def totalValue(x):
    print("The total of the list is: ", sum(x))
main()
