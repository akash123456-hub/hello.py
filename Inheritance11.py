class Person:
    def __init__(self,name,idnumber,salary,post):
        self.name = name
        self.idnumber = idnumber
        self.salary = salary
        self.post = post
    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)
class Employee(Person):
       def __init__(self,name,idnumber,salary,post):
          self.salary = salary
          self.post = post
       


          Person. __init__(self,name,idnumber,salary,post)
a = Employee("Akash",5001,20000,"Manager")
a.display()