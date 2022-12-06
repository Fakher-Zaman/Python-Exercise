# find(), index(), isalpha(), isdigit(), isalnum()

string = "Welcome Here"
print(string)

print("find() Function:")
print(string.find('e'))
print(string.find('e', 2))
print(string.find('e', 8))
print(string.find('e', 10))
print(string.find('z'))    # Not Found (Return -1)

print("index() Function:")
print(string.index('m'))
print(string.index('e', 2))
print(string.index('e', 8))
print(string.index('e', 10))
# print(string.index('a'))    # Not Found (Gives Error)

str1 = "Welcome"
str2 = "12345"
str3 = "Welcome123"
str4 = "@Welcome#123"

print("isalpha() Function:")
print(str1.isalpha())
print(str2.isalpha())
print(str3.isalpha())
print(str4.isalpha())

print("isdigit() Function:")
print(str1.isdigit())
print(str2.isdigit())
print(str3.isdigit())
print(str4.isdigit())

print("isalnum() Function:")
print(str1.isalnum())
print(str2.isalnum())
print(str3.isalnum())
print(str4.isalnum())
