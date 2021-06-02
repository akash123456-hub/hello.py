class Person:
    def __init__(self,fname,lname,add,city):
        self.firstname = fname
        self.lastname = lname
        self.address = add
        self.city = city
    def printname(self):
        print(self.firstname,self.lastname,self.address,self.city)
class Student(Person):
    def __init__(self,fname,lname,add,city):
      Person. __init__(self,fname,lname,add,city) 
x = Student("Akash","Kumar","C27/96 A Jagatganj","varanasi") 
x.printname()

