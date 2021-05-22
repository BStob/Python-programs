def main():
    writeToFile()
    appendToFile()

def writeToFile():
    i = 0
    file_object = open("names.txt", "w")
    while i != 9:
        file_object.write(input("Enter a name: "))
        file_object.write("\n")
        i = i + 1
    file_object.close()
    
def appendToFile():
    file_object = open("names.txt", "a")
    file_object.write("John Doe")
    file_object.write("\n")
    file_object.close()

main()
