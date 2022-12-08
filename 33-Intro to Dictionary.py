"""
    Myths about Dictionary:
    1 - Unordered Data Type
    2 - Working on key / value
    3 - Enclosed in Curly Brackets { }
    4 - Mutable Data Type (Change Data Type)
"""

dic = {
    'name': 'Python',
    'fee': 8000,
    'duration': '2 Months'
}

print(dic, type(dic))
print(dic['fee'])
print("--------------------")

# Get the data from dic by using for loop:
for n in dic:
    print("Key: ", n)
    print("Value: ", dic[n])
    print("--------------------")
