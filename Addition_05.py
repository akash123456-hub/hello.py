class Programmer:
    company = "Google"
    def __init__(self,name,age,salary,product):
        self.name = name
        self.age = age
        self.salary = salary
        self.product = product
    def getInfo(self):
        print(f"The programmer name is {self.name}")
        print(f"The programmer age is {self.age}")
        print(f"The programmer salary is {self.salary}")
        print(f"The programmer product is {self.product}")
harry = Programmer("Harry",30,2000,"Youtube")
harry.getInfo()
