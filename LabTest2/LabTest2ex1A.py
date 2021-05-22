import os
def getData():
    fileLocal = open("testdataC.csv", "r")
    for z in fileLocal:
        #Loops through the file until the name value is occupied by 'Ireland' it then prints all the values
        splitZ = z.split(',')
        if (splitZ[0] == "Malaysia"):
            break
    fileLocal.close()
    return splitZ

def dataHighDeaths24():
    y = 0
    i = 0
    #highCases is started with empty variables to be compared against the file.
    highCases = ["0", "0"]
    fileLocal = open("testdataC.csv", "r")
    y = fileLocal.readline()
    for y in fileLocal:
        splitY = y.split(',')
        i = i+1
        #Sets the highest case value along with the country name
        if float(highCases[1]) < float(splitY[6]):
            highCases.clear()
            highCases.append(splitY[0])
            highCases.append(splitY[6])
    fileLocal.close()
    print(highCases[0] + " " + "had the most reported deaths with" + " "+ highCases[1])

def dataHighDeaths100k():
    #This portion of the function stores all the values in a list and sorts them, it then removes all but the top 10
    varList = []
    i = 47
    fileLocal = open("testdataC.csv", "r")
    y = fileLocal.readline()
    for y in fileLocal:
        splitY = y.split(',')
        varList.append(float(splitY[3]))
        
    fileLocal.close()
    
    varList.sort()
    
    while i != 4:
        varList.pop(0)
        i = i - 1
        
    #This portion of the compares the data values against the file to get the names in the correct order
    c = 0
    namesList = []
    while c < 3:
        fileLocal = open("testdataC.csv", "r")
        y = fileLocal.readline()
        for y in fileLocal:
            splitY = y.split(',')
            if splitY[3] == '' or splitY[2] == '':
                continue
            elif varList[c] == float(splitY[3]):
                namesList.append(splitY[0])
        fileLocal.close()
        c = c + 1

    print('Highest deaths per 100000: ')
    for i in range(0,3):
        print(namesList[i] + ": " + str(varList[i]))



def dataMalaysia(x):
    print("The number of deaths in Malaysia in the last 24hrs: " + x[6])

    

def main():
    path = R"C:\Users\obieo\Documents\Downloads\Python programs\LabTest2"
    os.chdir(path)
    x = getData()
    dataMalaysia(x)
    dataHighDeaths24()
    dataHighDeaths100k()


main()