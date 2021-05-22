class Workers():
    def __init__(self, wname="", salary=0, tax=0):
        self.__worker_name = wname
        self.__salary = salary
        self.__tax = tax

    def setWorkerName(self, wname):
        self.__worker_name = wname

    def setSalary(self, salary):
        self.__salary = salary

    def getSalary(self):
        return (self.__salary)

    def calcTax(self):
         x = float(self.getSalary())*0.4
         return(x)
    
    def __str__(self):
        return(str(self.__worker_name) + "'s salary is: " + str(self.__salary) + " and their annual tax is: " + str(self.calcTax()))

