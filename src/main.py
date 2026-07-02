from models.employee import Employee

employees = []

employees.append(Employee("E001", "Sam", "sam@company.com", "IT"))
employees.append(Employee("E002", "John", "john@company.com", "HR"))

employees[0].change_department("Cyber Security")

for employee in employees:
    employee.display()