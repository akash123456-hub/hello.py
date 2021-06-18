class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self,num2):
        print("lets add")
        return self.num + num2.num
    def __mul__(self,num2):
        print("lets multiply")
        return self.num * num2.num
    def __div__(self,num3):
        print("lets devide")
        return self.num / num3.num
n1 = Number(10)
n2 = Number(6)
n3 = Number(2)
sum = n1 + n2
mul = n1 * n2
div = n1 / n3
print(sum)
print(mul)
print(div)