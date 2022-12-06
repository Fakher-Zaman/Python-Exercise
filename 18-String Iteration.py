# Method no. 1:
str1 = "BS Information Technology"
# str1 = str1[-1::-1]        # For reverse of string
length = len(str1)
print(length)

print("String in Same Order:")
for n in range(length):
    print(n, "-->", str1[n])

print("String in Reverse Order:")
for n in range(length-1, -1, -1):
    print(n, "-->", str1[n])

# Method no. 2:
str2 = "Hello World!"
print("String in Same Order:")
for n in str2:
    print(n)
print("String in Reverse Order:")
str2 = str2[-1::-1]
for n in str2:
    print(n)
