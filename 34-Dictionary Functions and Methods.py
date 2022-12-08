"""
For get element from dictionary:
    1 - get()
    2 - keys()
    3 - values()
    4 - items()
"""

dic = {
    'name': 'Fakhar Zaman',
    'class': 'BS Information Technology',
    'cgpa': 3.43
}
print(dic, type(dic))
print("\n")

# get()
result = dic.get('name')
print(result)
print("\n")

# keys()
for n in dic.keys():
    print("Key: ", n)
print("\n")

# values()
for n in dic.values():
    print("Value: ", n)
print("\n")

# items()
for n, m in dic.items():
    print(n, m)         # n for keys, m for values
print("--------------------------------------------------------------\n")

"""
For delete element from dictionary:
    1 - del
    2 - pop()
"""
# del
del dic['cgpa']
print(dic)

# pop()
a = dic.pop('class')
print(a)
print(dic)
print("--------------------------------------------------------------\n")

"""
Other important functions and methods of dictionary:
    1 - dict()
    2 - update()
    3 - clear()
"""
# dict()
d = dict(name='Hammad Asif', level='BS Information Technology', cgpa=2.70, friend="Fakher Zaman")
print(d)

d['description'] = "Both are best students of the year"

d.update(name='Fakher Zaman', cgpa=3.43, friend="Hammad Asif")
print(d)

d.clear()
print(d)
