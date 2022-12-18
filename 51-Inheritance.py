# Single Inheritance:
class A:
    def displayA(self):
        print("Welcome to class A")
class B(A):
    def displayB(self):
        print("Welcome to class B")

# Multi-Level Inheritance:
class C(B):
    def displayC(self):
        print("Welcome to class C")

# Multiple Inheritance:
class M1:
    def displayM1(self):
        print("Welcome to class M1")
class M2:
    def displayM2(self):
        print("Welcome to class M2")
class M(M1, M2):
    def displayM(self):
        print("Welcome to class M")

print("Single Inheritance:")
objB = B()
objB.displayA()
objB.displayB()

print("\nMulti-Level Inheritance:")
objC = C()
objC.displayA()
objC.displayB()
objC.displayC()

print("\nMultiple Inheritance:")
objM = M()
objM.displayM1()
objM.displayM2()
objM.displayM()