def computeAverage(x, y, z):
    totVal = int(x+y+z)
    avgVal = int(totVal)/3
    return avgVal
    

x = int(input("Enter an x value: "))
y = int(input("Enter an y value: "))
z = int(input("Enter an z value: "))
avgVal = computeAverage(x, y, z)
print("The average of those 3 values is: ", avgVal)
