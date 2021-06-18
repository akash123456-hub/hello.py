class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    Subunit = "Youtube"
    Age = 30
    def getLanguage(self):
        print(f"The language is {self.language}")
    def showDetails(self):
        print("This is an programmer")
    def showDetails(self):
        print(f"The subunit is {self.Subunit}")
    def showDetails(self):
        print(f"The Programmer age is {self.Age}")
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)
print(p.language)
print(p.Subunit)
print(p.Age)