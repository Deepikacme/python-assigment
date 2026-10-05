products = {
    "Laptop": 50000,
    "Pen": 20,
    "Bag": 1500,
    "Book": 500,
    "Watch": 2000
}

for product, price in products.items():
    if price > 1000:
        print(product, price)