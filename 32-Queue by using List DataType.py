# Implement a Stack and Queue Using a List Data Type
# Queue(First In First Out) Operation in Python:
List = []
while True:
    choice = int(input(
        '''
        Enter 1 for Push(Append) Element
        Enter 2 for Pop Element
        Enter 3 for Front(First) Element
        Enter 4 for Rear(End) Element
        Enter 5 for Display Queue
        Enter 6 for Exit
        '''
    ))
    if choice == 1:
        n = input("Enter the value: ")
        List.append(n)
        print(List)
    elif choice == 2:
        if len(List) == 0:
            print("Empty Queue!")
        else:
            del List[0]
            print(List)
    elif choice == 3:
        if len(List) == 0:
            print("Empty Queue!")
        else:
            print("First Queue Element: ", List[0])
    elif choice == 4:
        if len(List) == 0:
            print("Empty Queue!")
        else:
            print("Last Queue Element: ", List[-1])
    elif choice == 5:
        if len(List) == 0:
            print("Empty Queue!")
        else:
            print("Display Queue: ", List)
    elif choice == 6:
        break
    else:
        print("Invalid Operation!")
