from Students import L7Student, L8Student

def main():
    student1 = L7Student("Ben", "Stobie", 75)
    student2 = L8Student("Craig", "Doyle", 45)
    student3 = L7Student("Redas", "Strumila", 69)
    student4 = L8Student("Keith", "Butterly", 100)

    print("Level 7 Students:")
    print(student1)
    print(student3)
    print("Level 8 Students:")
    print(student2)
    print(student4)

if __name__ == "__main__":
    main()