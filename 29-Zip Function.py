# Zip Function - Iterate Over 2+ Lists at the Same Time
List1 = [1, 2, 3, 4, 5]
List2 = [6, 7, 8, 9, 10]
for a, b in zip(List1, List2):
    print(a, b)
print("--------------")

# Method # 2:
l1 = len(List1)
for x in range(l1):
    print(List1[x], List2[x])
