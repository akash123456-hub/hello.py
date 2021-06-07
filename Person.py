class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getDetails(self):
        print('Hello my name is',self.name,"and my age is",self.age)
p = Person("Akash",30)     
p.getDetails()   