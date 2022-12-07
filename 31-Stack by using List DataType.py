# Implement a Stack and Queue Using a List Data Type
# Stack(Last In First Out) Operation in Python:
List = []
while True:
    choice = int(input(
        '''
        Enter 1 for Push Element
        Enter 2 for Pop Element
        Enter 3 for Peek Element
        Enter 4 for Display Element
        Enter 5 for Exit
        '''
    ))
    if choice == 1:
        n = input("Enter the value: ")
        List.append(n)
        print(List)
    elif choice == 2:
        if len(List) == 0:
            print("Empty Stack!")
        else:
            p = List.pop()
            print(p)
            print(List)
    elif choice == 3:
        if len(List) == 0:
            print("Empty Stack!")
        else:
            print("Last Stack Value: ", List[-1])
    elif choice == 4:
        if len(List) == 0:
            print("Empty Stack!")
        else:
            print("Display Stack: ", List)
    elif choice == 5:
        break
    else:
        print("Invalid Operation!")
