class Employee:
    company = "google"
    ecode = 2
class Freelancer:
    company = "Fiverr"
    level = 0
    def upgradelevel(self):
     self.level = self.level+1
class Programmer(Employee,Freelancer):
     name = "Akash"
p = Programmer()
p.upgradelevel()
print(p.level)



