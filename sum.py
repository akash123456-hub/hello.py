class Number:
    def sum(self):
        return self.a + self.b
    def mul(self):
        return self.c * self.d

num = Number()
num.a = 34
num.b = 50
num.c = 80
num.d = 100
s1 = num.mul()
s = num.sum()
print(s1)
print(s)
