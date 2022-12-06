# --------If, If Else & If Elif Else-----------

# num = int(input("Enter a Number: "))
# if num % 2 == 0:
#     print(num, "is an even number.")
# else:
#     print(num, "is an odd number.")

marks = int(input("Enter Your Marks Out of 100 : "))
if marks > 100:
    print("Marks Out of Range")
elif marks >= 85:
    print("Grade A+")
elif marks >= 80:
    print("Grade A-")
elif marks >= 75:
    print("Grade B+")
elif marks >= 70:
    print("Grade B-")
elif marks >= 65:
    print("Grade C+")
elif marks >= 60:
    print("Grade C-")
elif marks >= 55:
    print("Grade D+")
elif marks >= 50:
    print("Grade D-")
else:
    print("Grade F")
