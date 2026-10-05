def product_price(price, quantity):
        if quantity <= 0:
            raise ValueError("Invalid quantity")
        total_price = price * quantity
        print("total price:",total_price)
print()
product_price(100,3)