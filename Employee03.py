class Employee:
    company = "Google"
    def __init__(self,name,product):
         self.name = name
         self.product = product
    def getInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")
akash = Employee("Akash","Gpay")
ruby = Employee("Ruby","Youtube")
akash.getInfo()
ruby.getInfo()
    