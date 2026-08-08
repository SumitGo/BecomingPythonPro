class Add():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b

class Sub(Add):
    def sub(self):
        return self.a - self.b

class Mul(Add):
    def mul(self):
        return self.a * self.b

class Div(Add):
    def div(self):
        return self.a // self.b
    

class Calculator(Add, Sub ):#, Sub, Mul, Div):
    def __init__(self, a, b):
        super().__init__(a, b)

print("1. Addition \n 2. Subtraction\n 3. Multiplication \n 4. Division")
option = int(input("Which Options do you want to perform"))
a = float(input("First Number"))
b= float(input("Second Number"))
calc = Calculator(a,b)
while option < 5:
    if option == 1:
        res = calc.add()
    elif option ==2:
        res = calc.sub()
        print(res)
    elif option == 3:
        res = calc.mul()
    elif option == 4:
        res = calc.div()
    else:
        break
    print(res)
    option = int(input("Do You Want to continue:"))
