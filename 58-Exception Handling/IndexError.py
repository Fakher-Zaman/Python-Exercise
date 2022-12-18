LIST = [10, 20, 30, 40]

try:
    print(LIST[9])
except IndexError:
    print("Index out of range here")
else:
    print("Nothing went wrong")
finally:
    print("End of try except handling!")