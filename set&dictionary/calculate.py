employees = {
    "Ravi": 30000,
    "Sita": 40000,
    "John": 50000
}

total = 0

for salary in employees.values():
    total += salary

average = total / len(employees)

print(average)