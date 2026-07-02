class Employee:

    def __init__(self, employee_id, name, email, department):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department

    def display(self):
        print("Employee ID :", self.employee_id)
        print("Name        :", self.name)
        print("Email       :", self.email)
        print("Department  :", self.department)
        print()

    def change_department(self, new_department):
        self.department = new_department