class InsufficientStockError(Exception):
    pass
    stock = 10
    quantity = int(input("Enter quantity: "))

    if quantity > stock:
        raise InsufficientStockError("Insufficient stock")
print("Product available")
print(e)