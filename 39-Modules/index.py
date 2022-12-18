# ---> Method # 1:
import module

print(module.sum(10, 20))
print(module.mul(10, 20))

# ---> Method # 2: 
# from module import sum
from module import *

print(sum(30, 20))
print(mul(30, 20))

# ---> Method # 3:
import module as m      # Making alias

print(m.sum(30, 40))
print(m.mul(30, 40))