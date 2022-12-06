"""
List in Python:
---------------
    => List is mutable
    => written in square brackets []
    => Separated by comma ,
"""

# Singly, 1 Dimensional or Simple list
list1 = [1, 2, 3, 4, 5]
list2 = [5, "Hello"]

# Doubly, 2 Dimensional or Nested list
list3 = [1, 2, 3, 4, 5, [5, "Hello"]]
list4 = [1, "Hello", 3, 4, 5, ["World!", 2], 3, 4, 5]

list4[8] = "O.K."        # mutable
# Indexing in list
print(list4[1], list4[3])
print(list4[5])
print(list4[6])
print("------------------------------------------")

# Slicing in list
print(list4[1:5])
print(list4[0:])
print(list4[4:7])
print(list4[0::2])       # [start:end:increment]
print(list4[-1::-1])     # In reverse case [end:start:decrement]
print("------------------------------------------")

# Nested list
list5 = [1, 2, 3, "Welcome", ["Brothers", 2, ["Ali", "Ahmad"], "OK"], 9, "Good Bye!"]
print(type(list5))
print(list5[4][2][1])    # 3 Dimensional
