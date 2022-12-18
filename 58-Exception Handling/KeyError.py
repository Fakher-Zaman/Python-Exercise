ages = {'Fakhar': 22, 'Fatima': 21, 'Yunus': 25}    # Dictionary DataType
person = input('Get age for: ')

try:
    print(f'{person} is {ages[person]} years old.')
except KeyError:
    print(f"{person}'s age is unknown.")