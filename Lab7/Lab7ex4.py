def main():
    i = 0
    names = open("names.txt", "r")
    while i != 10:
        read = names.readline()
        print(read)
        i = i + 1

    names.close()



main()
