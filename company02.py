class Employee:
    company = "Google"
    def showDetails(self):
        print("This is an employee")
class Programmer(Employee):
      language = "Python"
      def getLanguage(self):
        print(f"The language is {self.language}")
      def showDetails(self):
          print(f"This is an programmer")
e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.language)
print(p.company)
        

