class Student:
    # Constructor:
    def __int__(self):
        self.__name = ""
        self.__class = ""
    # Getters (Accessors):
    def getName(self):
        return self.__name
    def getClass(self):
        return self.__class
    # Setters (Mutators):
    def setName(self, a):
        self.__name = a
    def setClass(self, b):
        self.__class = b

ali = Student()
ali.setName("Ali Hamza")
ali.setClass("B.A")
name = ali.getName()
print("Name:", name)
level = ali.getClass()
print("Class:", level)
