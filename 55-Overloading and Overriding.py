# For Function Overloading:
class Area:
    def findArea(self, a = None, b = None):
        if a != None and b != None:
            print("Area of Rectangle:", (a * b))
        elif a != None:
            print("Area of Square:", (a * a))
        else:
            print("Nothing to Find!")

# For Function Overriding:
class A:
    def showData(self):
        print("I'm in A")

class B(A):
    def showData(self):
        print("I'm in B")

print("-> Method Overloading:")
obj1 = Area()
obj1.findArea()
obj1.findArea(10)
obj1.findArea(10, 20)

print("\n-> Method Overriding:")
obj2 = B()
obj2.showData()