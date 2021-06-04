class Employee:
 company = "Bharat Gas"
salary = 5600
salarybonus = 500
totalsalary = 6100
@property
def totalSalary(self):
      return self.salary + self.salarybonus
e = Employee()
print(e.totalsalary)



