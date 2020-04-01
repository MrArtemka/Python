# 1 Вариант
class Cal:
    def __init__(self):
        self.a = int(input())
        self.b = int(input())
        self.what = input()
    def Calculator(self):
        if self.what == '+':
            return self.a + self.b
        elif self.what == '-':
            return self.a - self.b
        elif self.what == '/':
            return self.a / self.b
        elif self.what == '*':
            return self.a * self.b
        
C = Cal()
print(C.Calculator())

# 2 Вариант

class Cal2:
    def Calculator2(self):
        a = int(input())
        b = int(input())
        what = input()
        if what == '+':
            return a + b
        elif what == '-':
            return a - b
        elif what == '/':
            return a / b
        elif what == '*':
            return a * b

C2 = Cal2()
print(C2.Calculator2())