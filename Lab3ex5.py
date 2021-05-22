i = 0

login = input("Please enter your username: ")

while i != 1:
    if login == "student1":
        i = 1  
    elif login == "student2":
        i = 1
    elif login == "student3":
        i = 1
    else:
        print("Invalid username!")
        login = input("Please enter your username: ")

passwrd = input("Please enter your password: ")

if login == "student1":
    while passwrd != "networking101":
        print("That's not your password")
        passwrd = input("Please enter your password: ")
elif login == "student2":
    while passwrd != "networking102":
        print("That's not your password")
        passwrd = input("Please enter your password: ")
else:
    while passwrd != "networking103":
        print("That's not your password")
        passwrd = input("Please enter your password: ")

print("Succesfully logged in")
