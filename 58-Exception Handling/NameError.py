def message():
    try:
        fullName = "Fakhar Zaman"
        return name
    except NameError:
        return "NameError occurred. Some variable isn't defined."
 
print(message())