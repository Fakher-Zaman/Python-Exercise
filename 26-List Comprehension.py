# By Normal Way:
List1 = []
for a in range(1, 101):
    # print(a)
    List1.append(a)

print(List1)

# By Comprehensive Way:
List2 = [b for b in range(1, 101) if b % 2 == 0]
print(List2)

text = "Hello World!"
List3 = [c for c in text]
print(List3)
