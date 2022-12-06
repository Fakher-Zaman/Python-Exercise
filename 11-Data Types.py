print("--> Numeric DataTypes:")
num = 10
print(num, type(num))
num = 10.5;
print(num, type(num))
num = 10+5j
print(num, type(num))

print("\n--> Sequence DataTypes:")      # Ordered Collection of Data
print("1.Strings:")       # Strings are Immutable (NoChange)
str1 = "Hello World!"
print(str1, type(str1))
str2 = '''Hello,
    Life is like a race, which we have learning different things.
okay!'''
print(str2, type(str2))

print("2.Lists:")         # Lists are Mutable (Change)
l1 = [10, 'abc', 5.5, 5+6j, 9]
l1[4] = '#'
print(l1, type(l1))

print("2.Tuples:")         # tuples are Immutable (NoChange)
t1 = ('ali', 500, 5.5)
print(t1, type(t1))
t2 = (5)          # int type
print(t2, type(t2))
# Tuples are faster than lists

print("\n--> Dictionary DataType:")       # UnOrdered Collection of Data
d = {
    'key': 'value',
    'course-name': 'Python',
    'course-duration': '3 Month'
}
print(d['key'])         # Dictionary is Mutable (Change)
print(d, type(d))

print("\n--> Sets DataType:")       # UnOrdered Collection of Data
my_set = {1, 2, 3, 4, 5, 2}       # Unique (No Duplicates)
print(my_set, type(my_set))       # Sets are Immutable (NoChange)

print("\n==> Booleans DataType:")
a = True
print(a, type(a))
b = False
print(b, type(b))
