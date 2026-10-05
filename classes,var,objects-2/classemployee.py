class Employee:
    company_name="TCS"
    employee_count=0
emp1=Employee()
Employee.employee_count+=1
emp2=Employee()
Employee.employee_count+=1
print(Employee.company_name)
print("Employees:",Employee.employee_count)