class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person1=Person("Deepika", 20, "Rajahmundry")
person2=Person("Priya", 21, "Vijayawada")

print("Name:",person1.name)
print("Age:",person1.age)
print("City:",person1.city)
print()
print("Name:",person2.name)
print("Age:",person2.age)
print("City:",person2.city)