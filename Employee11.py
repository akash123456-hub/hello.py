class Employee:
    company = "Google"
    def getDetails(self):
        print("This is an employee")
class Programmer(Employee):
    language = "python"
    def getLanguage(self):
        print(f"The language is {self.language}")
    def getDetails(self):
        print("This is an programmer")
e = Employee()
e.getDetails()
p = Programmer()
p.getDetails()
print(p.company)
