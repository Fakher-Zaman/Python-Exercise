import math

try:
    x = int(input('Please enter a positive number:\n'))
    try:
        print(f'Square Root of {x} is {math.sqrt(x)}')
    except ValueError as ve:
        print(f'You entered {x}, which is not a positive number.')
        
except ValueError as ve:
    print('You are supposed to enter positive number.')