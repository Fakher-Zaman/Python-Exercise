"""
=> Tuple is ordered data type.
=> Tuple is immutable (Not Change).
=> Tuple working according to index numbers.
=> Tuple created by using parenthesis ( ).
"""

t = (10, 20, 30, 40, 50, 10)
print(t, type(t))

a = t[2]
print(a)

length = len(t)
for n in range(length):
    print(n, t[n])
print("----------------------------------")

for n in t:
    print(n)
print("----------------------------------")

"""
There are the following type of functions that used in Tuple:
    1 - min()
    2 - max()
    3 - count()
    4 - index()
    5 - sum()    
"""

# min()
minNum = min(t)
print("Maximum Number: ", minNum)

# max()
maxNum = max(t)
print("Minimum Number: ", maxNum)

# count()
print("Count Number: ", t.count(10))

# index()
print("Index Number: ", t.index(40))

sumNums = sum(t)
print(sumNums)
