class Programmer:
    company = "Google"
    def __init__(self,name,product):
        self.name = name
        self.product = product
    def getDetails(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")
rajiv = Programmer("Rajiv","Gpay")
alka = Programmer("Alka","Youtube")
rajiv.getDetails()
alka.getDetails()
