class InvalidSalaryError(Exception):
    pass
    salary = int(input("Enter salary: "))

    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative")
print("Valid salary")
print(e)