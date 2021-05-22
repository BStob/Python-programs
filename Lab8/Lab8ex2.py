#Ben Stobie
#26 March 2021

def main():
    ipList = []
    inList = open("ipaddresses.txt", "r")
    readLine = inList.readline()
    while readLine:
        ipList.append(readLine.strip())
        readLine = inList.readline()
    print(ipList)
    ipSet = set(ipList)
    print(ipSet)
    inList.close()
main()
