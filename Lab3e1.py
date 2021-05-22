val = int(input("Please enter a value: "))
while val <= 0 or val >= 10:
    val = int(input("Please enter a valid input (between 1-10): "))

print(val)
