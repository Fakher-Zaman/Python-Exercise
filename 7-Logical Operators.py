x = 12
y = 24

print("-----Tautology-----")
print(x != y and x <= y)             # T
print(x == y or x != y)              # T
print(x != y and x <= y or x == y)   # T
print(not x == y)                    # T
print(not x == y or x > y)           # T
