from workers import Workers

def main():
    worker1 = Workers(input("Enter worker name: "), input("Enter worker salary: "))
    worker2 = Workers(input("Enter worker name: "), input("Enter worker salary: "))
    worker3 = Workers(input("Enter worker name: "), input("Enter worker salary: "))
    worker4 = Workers(input("Enter worker name: "), input("Enter worker salary: "))

    worker1.setSalary((int(worker1.getSalary())*2))
    worker2.setSalary((int(worker2.getSalary())*2))
    worker3.setSalary((int(worker3.getSalary())*2))
    worker4.setSalary((int(worker4.getSalary())*2))    

    print(worker1)
    print(worker2)
    print(worker3)
    print(worker4)

main()