#This is a piece of code developed by Ben Stobie, it's purpose is to etract relevant data from
#a .csv file using the python language and shows curent real time covid 19 data.
#Date: 16/04/21

import requests
import numbers
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def getFile():
    #Calls file download and writes it to a local csv file.
    x = requests.get('https://covid19.who.int/WHO-COVID-19-global-table-data.csv')
    fileLocal = open("WHO-COVID-19-global-table-data.csv", "w", encoding = "utf-8")
    fileLocal.write(x.text)
    fileLocal.close()
    

def extractIREData():
    fileLocal = open("WHO-COVID-19-global-table-data.csv", "r", encoding = "utf-8")
    for z in fileLocal:
        #Loops through the file until the name value is occupied by 'Ireland' it then prints all the values
        splitZ = z.split(',')
        if (splitZ[0] == "Ireland"):
            break
    
    print("Country: ", splitZ[0])
    print("Cases -  cumulative total: ", splitZ[2])
    print("Cases -  cumulative total  per 100000 population: ", splitZ[3])
    print("Cases -  Last 24hrs: ", splitZ[6])
    print("Cases -  Last 7 Days: ", splitZ[4])

    fileLocal.close()

    #Takes the above values and writes them to a text file
    fileLocal = open("Updated Data.txt", "w")
    fileLocal.write("Country: " + splitZ[0] + "\n")
    fileLocal.write("Cases -  cumulative total: " + splitZ[2] + "\n")
    fileLocal.write("Cases -  cumulative total  per 100000 population: " + splitZ[3] + "\n")
    fileLocal.write("Cases -  Last 24hrs: " + splitZ[6] + "\n")
    fileLocal.write("Cases -  Last 7 Days: " + splitZ[4] + "\n" + "\n")
    fileLocal.close()


def analyseAllData():
    y = 0
    i = 0
    avgSum = 0
    #highCases is started with empty variables to be compared against the file.
    highCases = ["0", "0"]
    fileLocal = open("WHO-COVID-19-global-table-data.csv", "r", encoding = "utf-8")
    y = fileLocal.readline()
    y = fileLocal.readline()
    #Occupied Palestinian territory includes a comma in the name, this messes with the split function
    #Hense this filter
    for y in fileLocal:
        splitY = y.split(',')
        if splitY[0] == '"occupied Palestinian territory':
            avgSum = avgSum + int(splitY[5])
        else:
            avgSum = avgSum + int(splitY[4])
        
        i = i+1
        #Sets the highest case value along with the country name
        if float(highCases[1]) < float(splitY[6]):
            highCases.clear()
            highCases.append(splitY[0])
            highCases.append(splitY[6])

    fileLocal.close()
    #Prints out the values and the average is printed to 2 decimal points
    totAvg = float(avgSum)/i
    correctDecimal = "{:.2f}".format(totAvg)
    print("Average of Cases in the last 7 days: ", correctDecimal)
    print("Highest cases in the last 24hrs: ", highCases[0])

    #Information is passed to the tet file
    fileLocal = open("Updated Data.txt", "a")
    fileLocal.write("Average of Cases in the last 7 days: " + correctDecimal + "\n")
    fileLocal.write("Highest cases in the last 24hrs: " + highCases[0] + "\n" + "\n")

    fileLocal.close()

    return i

def plotGraph(i):
    #This portion of the function stores all the values in a list and sorts them, it then removes all but the top 10
    varList = []
    fileLocal = open("WHO-COVID-19-global-table-data.csv", "r", encoding = "utf-8")
    y = fileLocal.readline()
    y = fileLocal.readline()
    for y in fileLocal:
        splitY = y.split(',')
        if splitY[0] == '"occupied Palestinian territory':
            varList.append(float(splitY[4]))
        elif splitY[3] == '' or splitY[2] == '':
            print(splitY[3])
            continue
        else:
            varList.append(float(splitY[3]))
    fileLocal.close()
    
    varList.sort()
    while i != 11:
        varList.pop(0)
        i = i - 1
        
    #This portion of the compares the data values against the file to get the names in the correct order
    c = 0
    namesList = []
    while c < 10:
        fileLocal = open("WHO-COVID-19-global-table-data.csv", "r", encoding = "utf-8")
        y = fileLocal.readline()
        y = fileLocal.readline()
        for y in fileLocal:
            splitY = y.split(',')
            if splitY[3] == '' or splitY[2] == '':
                continue
            elif varList[c] == float(splitY[3]):
                namesList.append(splitY[0])
        fileLocal.close()
        c = c + 1
    if namesList[0] == 'Saint BarthÃ©lemy':
        namesList.pop(0)
        namesList.insert(0, 'Saint Barthélemy')


    i = 9
    #This data is written in text form to the txt document
    fileLocal = open("Updated Data.txt", "a")
    fileLocal.write("Highest cases per 100000 population: " + "\n")
    fileLocal.close()
    while i >= 0:
        fileLocal = open("Updated Data.txt", "a")
        fileLocal.write(str(namesList[i]) + ": " + str(varList[i])+ "\n")
        fileLocal.close()
        i = i - 1


    #And is then plotted as a barchart
    names = namesList
    values = varList
    plt.rcParams.update({'font.size': 5})
    plt.bar(names, values)
    plt.xlabel("Countries")
    plt.ylabel("Cases (per 100000 population")
    plt.show()
    
def main():
    getFile()
    extractIREData()
    i = analyseAllData()
    plotGraph(i)

main()
