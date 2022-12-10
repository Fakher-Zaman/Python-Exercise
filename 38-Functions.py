"""
Types of Functions:
    1) Built-In Functions
    2) User-Defined Functions

Types of User-Defined Functions:
    ---> Simple Function
    ---> Function With Arguments
    ---> Return Type Function
"""

# Simple Function:
print("---> Simple Function: ")
def simpleFunction():         # Function Define
    print("Welcome to python!")

simpleFunction()              # Functions Call

# Function With Arguments:
print("---> Function With Argument: ")
def sumNumbers(a, b=5):       # Set Default Value
    sum = a + b
    print(sum)

sumNumbers(10)
sumNumbers(10, 20)
sumNumbers(20, 80)

# Return Type Function:
print("---> Return Type Function: ")
def square(x):
    return x*x

data = square(20)
print(data)
