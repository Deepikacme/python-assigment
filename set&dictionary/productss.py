products = {
    "Pen": 20,
    "Book": 5,
    "Bag": 8,
    "Pencil": 15
}

for product, quantity in products.items():
    if quantity < 10:
        print(product, quantity)