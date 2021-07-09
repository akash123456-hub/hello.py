class Employee:
    company = "Google"
    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
    def showDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary} \n{signature}")
akash = Employee("Akash",30000,"Youtube")
akash.showDetails()