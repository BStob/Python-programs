i = 0
while i < 3:
    x = int(input("Enter the host number: "))
    if x < 1:
        print("The number is too low")

    elif x > 254:
        print("The number is too high")

    else:
        print("Valid number: ", x)
    i = i+1
    
        
