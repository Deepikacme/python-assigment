quantity=int(input("Enter quantity: "))
if quantity<= 0:
        raise ValueError("Quantity must be greater than zero")
print("Valid quantity")
print(not quantity  < 0)