class Employee:
    company = "Google"
    def getInfo(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")
harry = Employee()
harry.salary = 10000
harry.getInfo()