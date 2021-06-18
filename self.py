class Employee:
    company = "Google"
    def getsalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary} ")
        print(f"Salary for this employee in {self.company} is {self.salary}")
        print("Akash is good boy")
harry = Employee()
harry.salary = 20000
harry.getsalary()
Rohini = Employee()
Rohini.salary = 10000
Rohini.company = "Youtube"
Rohini.getsalary()