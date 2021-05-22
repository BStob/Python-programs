import pandas as pd
import os
import webbrowser
import sys
import numbers

def getFile():
    fileLocal = pd.ExcelFile("Content Links.xlsx")
    read_val = pd.read_excel(fileLocal, sheet_name=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])
    print(read_val[0])#.at[5, 'Product Link. http://'])
    return read_val

def determineCustomer(x):
    print('At the Post : 0')
    print('Bangor-On-Dee : 1')
    print('Bet Central : 2')
    print('Bar One : 3')
    print('BGBet : 4')
    print('Britbet : 5')
    print('Boylesports : 6')
    print('Chester : 7')
    print('Corbetts : 8')
    print('Gold Standard : 11')
    print('Subero : 13')
    print('Megabet : 14')
    print('PA : 16')
    print('Paddy Power : 17')
    print('Ryan Holmes : 18')
    print('S&D : 20')
    print('Toals : 22')
    print('Winning Post : 23')

    id_var = int(input("Please select a customer: "))
    while isinstance(id_var, numbers.Number) != True:
         print(isinstance(id_var, numbers.Number))
         id_var = input("Please select a customer: ")

    while int(id_var) > 23 or int(id_var) < 0:
         print("*Error Not a customer*")
         id_var = input("Please select a customer: ")

    if id_var == 0:
        at_the_post(x, id_var)
    elif id_var == 1:
        Bangor_On_Dee(x, id_var)
    elif id_var == 2:
        Bet_Central(x, id_var)
    elif id_var == 3:
        Bar_One(x, id_var)
    elif id_var == 4:
        BGBet(x, id_var)
    elif id_var == 5:
        Britbet(x, id_var)
    elif id_var == 6:
        Boylesports(x, id_var)
    elif id_var == 7:
        Chester(x, id_var)
    elif id_var == 8:
        Corbetts(x, id_var)
    elif id_var == 11:
        Gold_Standard(x, id_var)
    elif id_var == 13:
        Subero(x, id_var)
    elif id_var == 14:
        Megabet(x, id_var)
    elif id_var == 16:
        PA(x, id_var)
    elif id_var == 17:
        Paddy_Power(x, id_var)
    elif id_var == 18:
        Ryan_Holmes(x, id_var)
    elif id_var == 20:
        SandD (x, id_var)
    elif id_var == 22:
        Toals(x, id_var)
    elif id_var == 23:
        Winning_Post(x, id_var)
        
    print("Data was excluded - update spreadsheet")

def at_the_post(x, id_var):
    i = 0
    while i != 5:
        url = x[id_var].at[i, 'Product Link. http://']
        y = url.split('/')
        v = y[5]
        print(v)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Bangor_On_Dee(x, id_var):
    i = 0
    while i != 5:
        url = x[id_var].at[i, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Bet_Central(x, id_var):
    i = 0
    while i != 8:
        url = x[id_var].at[i, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Bar_One(x, id_var):
    i = 0
    while i != 7:
        url = x[id_var].at[i, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def BGBet(x, id_var):
    i = 0
    while i != 6:
        url = x[id_var].at[i, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Britbet(x, id_var):
    i = 92
    while i != 97:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Boylesports(x, id_var):
    i = 4
    while i != 13:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Chester(x, id_var):
    i = 1
    while i != 2:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Corbetts(x, id_var):
    i = 9
    while i != 18:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Gold_Standard(x, id_var):
    i = 9
    while i != 18:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Subero(x, id_var):
    i = 8
    while i != 15:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Megabet(x, id_var):
    i = 7
    while i != 12:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def PA(x, id_var):
    i = 0
    while i != 1:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Paddy_Power(x, id_var):
    i = 0
    while i != 6:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Ryan_Holmes(x, id_var):
    i = 6
    while i != 10:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def SandD (x, id_var):
    i = 10
    while i != 19:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Toals(x, id_var):
    i = 10
    while i != 19:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()

def Winning_Post(x, id_var):
    i = 9
    while i != 19:
        url = x[id_var].at[2, 'Product Link. http://']
        y = url.split('/')
        print(y)
        #webbrowser.open('http://' + url, new=2, autoraise=True)
        i = i + 1
    sys.exit()



def main():
    path = R"C:\Users\obieo\Documents\Downloads\Python programs\Personal Projects"
    os.chdir(path)
    extracted_values = getFile()
    determineCustomer(extracted_values)


    



main()
