#Ben Stobie
#26 March 2021

def main():
    emptDic = {}
    split2 = []
    i = 0
    x = 0
    inStr = open("ifacedata.json", "r")
    readLine = inStr.read()
    readLine = readLine.strip('{')
    strip1 = readLine.strip('} \n')
    split1 = strip1.split(',')
    for i in range(len(split1)):
        split2.append(split1[i].split(':'))
    i = 0
    for x in range(3):
        emptDic[split2[x][i]] = split2[x][i+1]
        
    
    print(emptDic)
        
main()
