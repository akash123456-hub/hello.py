class Employee:
    company = "Google"
    salary = 3000
alka = Employee()
rehman = Employee()
alka.salary = 4000
rehman.salary = 5000
print(alka.company)
print(rehman.company)
Employee.company = "Youtube"
print(alka.company)
print(alka.salary)
print(rehman.company)
