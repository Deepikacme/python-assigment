class InvalidQuantityError(Exception):
    pass

class ShoppingCart:
    def add_product(self, product, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Invalid quantity")
        print(product, "added to cart")

try:
    cart = ShoppingCart()
    cart.add_product("Bag", 2)
except InvalidQuantityError as e:
    print(e)