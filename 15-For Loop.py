# -----> Concept of Range in For Loop

# if range(5)
# then
# start = 0
# condition < 5
# increment of 1
# result = 0, 1, 2, 3, 4
for i in range(5):
    print(i)
print("\n")

# if range(1, 7)
# then
# start = 1
# condition < 7
# increment of 1
# result = 1, 2, 3, 4, 5, 6
for i in range(1, 7):
    print(i)
print("\n")

# if range(1, 10, 2)
# then
# start = 0
# condition < 10
# increment of 2
# result = 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i)
print("\n")

# Print a Table of any Number
num = int(input("Enter a number: "))
print("*******_Table of a number_*******")
for n in range(1, 11):
    print(num, "*", n, "=", num * n)
print("\n")

# -----> Concept of Range in Reverse Case

# if range(10, 0, -1)
# then
# start = 10
# condition > 0
# decrement of -1
# result = 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
for i in range(10, 0, -1):
    print(i)
