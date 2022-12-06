num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
opr = input('''
Enter the Operator
+ for Addition
- for Subtraction
* for Multiplication
/ for division
:''')

if opr == "+":
    print("Sum of Numbers =", (num1 + num2))
elif opr == "-":
    print("Sum of Numbers =", (num1 - num2))
elif opr == "*":
    print("Sum of Numbers =", (num1 * num2))
elif opr == "/":
    print("Sum of Numbers =", (num1 / num2))
else:
    print("Invalid Operation!")
