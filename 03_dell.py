class Employee:
    company = "Google"
    def getsalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")
harry = Employee()
harry.salary = 30000
harry.getsalary()