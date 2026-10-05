products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Pen": 20,
    "Bag": 1500,
    "TV": 30000
}

expensive = set()

for product, price in products.items():
    if price > 5000:
        expensive.add(product)

print(expensive)