class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def getinfo(self):
        print(f"The employee name is {self.name}")
        print(f"The employee age is {self.age}")
        print(f"The employee salary is {self.salary}")
class Programmer(Employee):
    def __init__(self,address):
        self.add = address
    def showDetails(self):
        print(f"The programmer address is {self.add}")
akash = Programmer("Akash",30,30000,"Varanasi")
akash.getInfo()