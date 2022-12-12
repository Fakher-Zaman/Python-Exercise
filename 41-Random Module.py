import random

print(random.randint(1, 10))
print(random.randrange(1, 10))

List = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(random.choice(List))

print("---> Modules: ")
print("random(): ", random.random())
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("shuffle(): ", random.shuffle(l))
print("uniform(): ", random.uniform(3, 9))
