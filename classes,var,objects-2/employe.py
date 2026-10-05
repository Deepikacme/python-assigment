class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

emp1 = Employee("Ravi", "HR", 30000)
emp2 = Employee("Priya", "IT", 40000)
emp3 = Employee("Kiran", "Finance", 35000)
emp4 = Employee("Anjali", "Sales", 32000)
emp5 = Employee("Rahul", "IT", 45000)

print(emp1.name, emp1.department, emp1.salary)
print(emp2.name, emp2.department, emp2.salary)
print(emp3.name, emp3.department, emp3.salary)
print(emp4.name, emp4.department, emp4.salary)
print(emp5.name, emp5.department, emp5.salary)