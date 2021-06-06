class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# harry.salary = 300
# rajni.salary = 400
harry.salary = 45
#rajni.address = "vns"
print(harry.salary)
print(rajni.salary)
#print(rajni.address)

# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 