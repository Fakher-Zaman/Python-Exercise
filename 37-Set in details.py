"""
=> Set is UnOrdered + UnIndexed Data Type.
=> Set defined by curly brackets OR We also created by using set() function.
=> Set used unique type of data.
"""

s = {10, 20, 30, 10, "Hello"}
print(s, type(s))

for n in s:
    print(n)
print("--------------------------------------------------")

"""
The following functions of set are involved in python:
1 - set()
2 - add()
3 - pop()
4 - remove()
5 - clear()
6 - discard()
7 - update()
"""

# set()
List = [10, 20, 30, 40, 50]
Set = set(List)
print("set(): ", List, Set)
print("--------------------------------------------------")

# add()
s = {40, 10, 20, 30}
s.add(50)
print("add(): ", s)
print("--------------------------------------------------")

# pop()
print("pop(): ", Set.pop())
print("pop(): ", Set.pop())
print(Set)
print("--------------------------------------------------")

# remove()
Set.remove(20)
print(Set)
print("--------------------------------------------------")

# discard()
Set.discard(30)
print(Set)
print("--------------------------------------------------")

# clear()
s.clear()
print(s)
print("--------------------------------------------------")

# clear()
List2 = ["Hello World!", 10, 20, "Okay"]
Set.update(List2)
print(Set)
print("--------------------------------------------------")
