class StockError(Exception):
    pass
stock=5
qty=int(input("Enter quantity: "))

raise StockError("Insufficient stock")
print("Product added")
print(e)