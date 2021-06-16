class Freelancer:
    company = "Fiverr"
    level = 0
    def upgradeLevel(self):
        self.level = self.level + 1
class Employee:
    company = "visa" 
    ecode = 121
class Programmer(Freelancer,Employee):
    name = "Akash"
p = Programmer()
p.upgradeLevel()
print(p.company)
