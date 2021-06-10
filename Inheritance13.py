class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)

class son(Mother,Father,Grandfather):
    def parents(self):
        print("Father:",self.fathername)
        print("Mother:",self.mothername)
        print("Grandfather:",self.grandfather)
s1 = son()  
s1.fathername = "Ram" 
s1.mothername = "sita"  
s1.grandfather = "Jignesh"
s1.parents()   


