class Employee:
    company = "Google"
    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!") 
    def showDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The employee subunit {self.subunit}")
class Programmer(Employee):
    def __init__(self,age):
         self.age = age
    def showDetails(self):
        print(f"The age of programmer is {self.age}")
ravi = ("Ravi", 20000,"Youtube")
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()


    