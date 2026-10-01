class Car:
    company="Toyota"
    number_of_wheels=4

    def __init__(self,model,price):
        self.model=model
        self.price=price

car1=Car("BMW",5000000)
print(car1.company)
print(car1.number_of_wheels)
print(car1.model)
print(car1.price)