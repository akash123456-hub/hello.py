class Employee:
    company = "Google"
    salary = 30000
harry = Employee()
alka = Employee()
harry.salary = 40000
alka.company = "Youtube"
print(harry.salary)
print(alka.salary)
print(alka.company)
print(harry.company)
