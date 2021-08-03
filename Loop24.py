class Employee:
    company = "Google"
    def getSalary(self):
        print(f"The salary of this employee working in {self.company} is {self.salary}")
harry = Employee()
harry.salary = 4000
harry.getSalary()