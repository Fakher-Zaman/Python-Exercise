# Python Program to Convert String to a List:
text = input("Enter the value: ")
print("String : ", text)
List1 = text.split()
print("List1 : ", List1)
print("-----------------------------------------\n")

List2 = []
for n in range(1, 5):
    a = input("Enter the value " + str(n) + ": ")
    List2.append(a)
print(List2)