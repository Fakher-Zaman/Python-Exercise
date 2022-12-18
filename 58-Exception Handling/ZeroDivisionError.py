try:
    print(10 / 0)
except ZeroDivisionError:
    print("Logical Error, Number is divided by zero!")
else:
    print("Nothing Went Wrong")
finally:
    print("The 'try except' is finished")