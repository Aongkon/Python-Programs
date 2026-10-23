from menu import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = [] # eta amader database
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
            print("----------------------------------")
            print("Employee List!!")
            for emp in self.employees:
                print(f"Name: {emp.name}\nPhone: {emp.phone}\nEmail: {emp.email}\nAddress: {emp.address}\nAge: {emp.age}\nDesignation: {emp.designation}\nSalary:{emp.salary}")
