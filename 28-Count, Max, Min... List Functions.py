# Count, Max, Min, Sort, Reverse & Index List Function:
print("\n---> count() Function:")
List1 = [10, 20, 30, 10, 40, 50, 10]
countValue = List1.count(10)
print(countValue)

print("\n---> max() Function:")
maxValue = max(List1)
print(maxValue)
List2 = ["Hello", "World!"]
maxValue = max(List2)
print(maxValue)

print("\n---> min() Function:")
minValue = min(List1)
print(minValue)
List2 = ["Hello", "World!"]
minValue = min(List2)
print(minValue)

print("\n---> sort() Function:")
List1.sort()
print(List1)

print("\n---> reverse() Function:")
List2.reverse()
print(List2)
List3 = [50, 10, 30, 40, 20, 60]
List3.reverse()
print(List3)

print("\n---> index() Function:")
print(List3.index(20))
