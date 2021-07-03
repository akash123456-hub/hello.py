class Employee:
    company = "Google"
    def getsalary(self,signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")
    @staticmethod
    def greet():
        print("Good morning sir")
    @staticmethod
    def time():
        print("The time is 9 AM in the morning")
harry = Employee()
harry.salary = 100000
harry.getsalary("Thanks")
harry.greet()
harry.time()