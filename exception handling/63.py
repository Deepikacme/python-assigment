class InvalidSalaryError(Exception):
    pass
    def __init__(self, salary):
        if salary < 0:
            raise InvalidSalaryError("Salary cannot be negative")
        self.salary=salary
print("Valid salary")
