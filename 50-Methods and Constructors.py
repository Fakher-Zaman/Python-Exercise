class DemoClass:
    a = 10

    def __init__(self):
        print("Welcome to Constructor!")
    def showValue(self):
        self.c = self.a * self.a
        print(self.c)
    def sumDisplay(self, a, b):
        print("Sum = ", a + b)

obj = DemoClass()
obj.showValue()
obj.sumDisplay(5, 10)