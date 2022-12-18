class Py:
    def displayInfo(self, name = ''):
        print("Welcome to the computer language:", name)
class Modern(Py):                   # Inheritance
    def displayInfo(self, name = ''):
        # super().displayInfo()       # Parent Function Calling
        print("Welcome to the modern language:", name)

# Method Overloading:
print("---> Method Overloading:")
obj = Py()
obj.displayInfo()
obj.displayInfo('Python')

# Method Overriding:
print("\n---> Method Overriding:")
objM = Modern()
objM.displayInfo()
objM.displayInfo('Python AI')