import urllib.request
def main():
    url = input("Please enter a valid URL: ")
    
    try:
        response = urllib.request.urlopen(url)
        alldata = response.read().decode('utf-8')
        print (alldata)
    except:
        print ("Something went wrong!") 

main()
