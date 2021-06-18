class Number:
    def sum(self):
        return self.a + self.b + self.c

num = Number()
num.a = 12
num.b = 34
num.c = 67
s = num.sum()
print(s)