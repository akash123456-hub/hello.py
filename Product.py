class Programmer:
    company = "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product
    def showDetails(self):
            print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")
akash = Programmer("Akash","skype")   
sita = Programmer("Sita","Github")    
akash.showDetails()    
sita.showDetails() 