class Employee:
    company = "Google"
    def getsalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")
akash = Employee()
akash.salary = 20000
akash.getsalary()