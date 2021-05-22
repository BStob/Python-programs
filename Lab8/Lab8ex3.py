#Ben Stobie
#26 March 2021

def main():
    users = {"student1" : "networking101", "student2" : "networking102", "student3" : "networking103"}
    i = 0
    while i != 1:
        x = input("Please enter your username: ")
        y = input("Please enter your password: ")
        if x in users:
            if users[x] != y:
                print("Invalid username or password")
            else:
                print("Logged In")
                i = 1
        else:
           print("Please create an account")
    
main()
