employees = {
    "Ravi": 45000,
    "Sita": 60000,
    "John": 75000
}

for name, salary in employees.items():
    if salary > 50000:
        print(name, salary)