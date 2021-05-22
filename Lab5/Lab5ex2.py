def main():
    i = 0
    x = input(str("Enter a string: "))
    print("The string written in reverse is: ")
    f = len(x)-1
   
    for i in range(len(x), 0, -1):
        print(x[f])
        f = f-1
main()
        
