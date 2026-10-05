subject1 = {
    "Ravi": 80,
    "Sita": 90,
    "John": 75
}

subject2 = {
    "Sita": 85,
    "John": 80,
    "Anu": 70
}

students1 = set(subject1.keys())
students2 = set(subject2.keys())

common = students1.intersection(students2)

print(common)