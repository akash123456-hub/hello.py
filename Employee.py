class Employee:
    company = "Google"
    salary = 300
akash = Employee()
Rajni = Employee()
akash = Employee()
Rajni = Employee()
akash.employeeid = 15002
Rajni.employeeid = 15001
akash.salary = 100
Employee.company = "Youtube"
#Rajni.salary = 222
print(akash.salary)
print(Rajni.salary)
print(akash.employeeid)
print(akash.company)