data = ["Hello", "Students", 578, 582, 552, "Roll Numbers"]
print("Type:", type(data), "Length:", len(data))
val = len(data)
print(val)

# Method no. 1
for iterate in range(val):
    print(data[iterate])
print("-------------")

# Method no. 2
for n in data:
    print(n)
print("-------------")

# Print in reverse order
for i in range(val-1, -1, -1):
    print(data[i])
