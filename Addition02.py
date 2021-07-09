class Number:
    def sum(self):
        return self.a + self.b
    def mul(self):
        return self.c * self.d

num = Number()
num.a = 12
num.b = 34
num.c = 52
num.d = 100
s = num.sum()
s1 = num.mul()
print(s)
print(s1)
