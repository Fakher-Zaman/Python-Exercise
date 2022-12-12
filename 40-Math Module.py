import math

x = 10.2
print("ceil(): ", math.ceil(x))
print("floor(): ", math.floor(x))

x = -12
print("fabs(): ", math.fabs(x))

x = 4
print("factorial(): ", math.factorial(x))      # 4! = 4*3**2*1 = 24

List = [10, 20, 30, 40]
print(type(List), math.fsum(List))
Set = {10, 20, 30, 40, 50}
print(type(Set), math.fsum(Set))
Tuple = (10, 20, 30)
print(type(Tuple), math.fsum(Tuple))

num = 16
print("num(): ", math.sqrt(num))