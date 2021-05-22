def main():
    x = 1
    whole = input("Enter a whole Number: ")
    try:
        z = x + int(whole)
    except:
        print("False")
        z = "NaN"
    else:
        z = int(whole)
    
    print("The value is: ", z)

main()
