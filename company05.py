class Person:
    def __init__(self,name,idnumber,salary,post,age):
        self.name = name
        self.idnumber = idnumber
        self.salary = salary
        self.post = post
        self.age = age
    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)
        print(self.age)
class Employee(Person):
    def __init__(self,name,idnumber,salary,post,age):  
        self.salary = salary
        self.post = post   
        Person. __init__(self,name,idnumber,salary,post,age)
a = Employee('Akash',22001,30000,"Manager",30)
a.display()

