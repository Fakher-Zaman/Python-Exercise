import random

compNumber = random.randrange(1, 101)
userNumber = int(input("Enter a number b/w (1-100): "))

if userNumber > compNumber:
    print("Computer number", compNumber)
    print("Your guess number is high!")
elif userNumber < compNumber:
    print("Computer number", compNumber)
    print("Your guess number is low!")
else:
    print("Computer number", compNumber)
    print("Your guess number is equal.")