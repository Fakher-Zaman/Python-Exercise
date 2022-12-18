class Student:
    __name = "Fakhar Zaman"  # Private Variable

    def __display(self):     # Private Method/Function 
        print("Welcome to Python!")
    
    def __init__(self):      # Constructor
        print(self.__name)
        self.__display()

obj = Student()
