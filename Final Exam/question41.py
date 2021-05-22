def readFile():
    fileInput = open("addresses.txt", "r")
    x = fileInput.read()
    fileInput.close()
    return(x)

def getValidIps(fileInput):
    goodIPs = []
    badIPs = []
    i = 0

    x = fileInput.split("\n")
    for i in x:
        z = i.split(".")
        if len(z[0]) < 1 or len(z[0]) > 3:
            badIPs.append(z[0] + "." + z[1] + "." + z[2] + "." + z[3])
            continue
        elif len(z[1]) < 1 or len(z[1]) > 3:
            badIPs.append(z[0] + "." + z[1] + "." + z[2] + "." + z[3])
            continue
        elif len(z[2]) < 1 or len(z[2]) > 3:
            badIPs.append(z[0] + "." + z[1] + "." + z[2] + "." + z[3])
            continue
        elif len(z[3]) < 1 or len(z[3]) > 3:
            badIPs.append(z[0] + "." + z[1] + "." + z[2] + "." + z[3])
            continue
        elif z[0] == " " or z[1] == " " or z[2] == " " or z[3] == " ":
            badIPs.append(z[0] + "." + z[1] + "." + z[2] + "." + z[3])
            continue
        elif len(z) > 4:
            badIPs.append(z[0] + "." + z[1] + "." + z[2] + "." + z[3] + "." + z[4])
            continue
        elif int(z[0]) < 0 or int(z[0]) > 255:
            badIPs.append(z[0] + "." + z[1] + "." + z[2] + "." + z[3])
            continue
        elif int(z[1]) < 0 or int(z[1]) > 255:
            badIPs.append(z[0] + "." + z[1] + "." + z[2] + "." + z[3])
            continue
        elif int(z[2]) < 0 or int(z[2]) > 255:
            badIPs.append(z[0] + "." + z[1] + "." + z[2] + "." + z[3])
            continue
        elif int(z[3]) < 0 or int(z[3]) > 255:
            badIPs.append(z[0] + "." + z[1] + "." + z[2] + "." + z[3])
            continue
        else:
            goodIPs.append(z[0] + "." + z[1] + "." + z[2] + "." + z[3])
    for i in badIPs:
        print("This IP is invalid: " + i)
    return goodIPs

def checkTUDAddress(x):
    i = 0
    for i in x:
        y = i.split(".")
        if int(y[0]) == 147:
            if int(y[1]) == 252:
                print(i + ": Valid TU Dublin IPv4 address")
        else:
            print(i + ": Valid IPv4 address")



def main():
    fileInput = readFile()
    validIps = getValidIps(fileInput)
    checkTUDAddress(validIps)
    print("IP address checking completed")


main()