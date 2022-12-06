# Function for Delete Element from List1 (del, pop(), remove(), clear()):
List1 = [10, 20, 30, 40, 50, 60]
print(List1)

del List1[1]
print("del =", List1)

List1.pop(1)
print("pop() =", List1)

List1.remove(50)
print("remove() =", List1)

List1.clear()
print("clear() =", List1)
print("-------------------------------")

# Function for Update Element from List2 (insert(), append(), extend()):
List2 = ["Hello", "World!", 200]
List2[2] = "Welcome"
print(List2)

List2.insert(2, 502)
print("insert() =", List2)

newList = [10, 20, 30]
List2.append(newList)
print("append() =", List2)

List2.extend(newList)
print("extend() =", List2)
