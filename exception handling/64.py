class InsufficientStockError(Exception):
    pass
    def __init__(self, stock):
        self.stock = stock

    def buy(self, quantity):
        if quantity > self.stock:
            raise InsufficientStockError("Insufficient stock")
        print("Product purchased")
        print ("remaining stock:",self.stock-quantity)
        p=InsufficientStockError(10)
    print.buy(15)
print(not 10>15)