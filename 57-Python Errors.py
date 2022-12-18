'''
These errors can be broadly classified into two classes:
=> Syntax Errors
=> Logical Errors (Exceptions)
'''

# Python Syntax Errors (Not Handled):
a = 10
b = 20
# if a == b   # Syntax Error (: not here) 
#     print("No")
# else        # Syntax Error (: not here) 
#     print("Yes")

# Python Logical Errors (Handled by Exception):
print(1 / 0)    # ZeroDivisionError: division by zero
LIST = [10, 20, 30, 40]
print(LIST[6])  # Index Error