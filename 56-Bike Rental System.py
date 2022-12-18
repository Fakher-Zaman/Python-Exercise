class BikeShop:
    def __init__(self, stock):
        self.stock = stock

    def displayBike(self):
        print("Total Bikes:", self.stock)

    def rentForBike(self, qty):
        if qty <= 0:
            print("Enter the value greater than 0:")
        elif qty > self.stock:
            print("Enter the value (less than stock)")
        else:
            print("Total Price:", qty * 100)
            self.stock -= qty
            print("Total Bikes:", self.stock)

while True:
    obj = BikeShop(100)        # 100 = stocks
    choose = int(input('''
    Enter
    1 for Display Stock
    2 for Rent a Bike
    3 for Exit
    :'''))

    if choose == 1:
        obj.displayBike()
    elif choose == 2:
        n = int(input("Enter the Quantity: "))
        obj.rentForBike(n)
    else:
        break