class Addition:
    first = 0
    second = 0
    answer = 0
    def __init__(self,f,s):
        self.first = f
        self.second = s
    def display(self):
        print("First number = " + str(self.first))
        print("second number = "+ str(self.second))
        print("Addition of the two numbers ="+ str(self.answer))
    def calculate(self):
        self.answer = self.first + self.second
obj = Addition(2000,1000)
obj.calculate()
obj.display()