list = ["Fakhar", "Hammad", "Shaban"]
indices = [0, 1, "2"]

for i in range(len(indices)):
    try:
        print(list[indices[i]])
    except TypeError:
        print("TypeError: Check list of indices")