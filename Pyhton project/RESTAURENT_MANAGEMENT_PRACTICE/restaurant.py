from menu import Menu
class Restaurant():
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()  # ey Menu class e parameter user theke anbo

    def add_employee(self, employee):
        self.employees.append(employee) # admin.add_employee theke ey employee golo astase

    # def remove_employee(self, employee):
    #     self.employees.remove(employee)
    def view_employee(self):
        print("----------------------------------")
        print("Employee List!!")

        for emp in self.employees:
            print(f"Name: {emp.name}\nPhone: {emp.phone}\nEmail: {emp.email}\nAddress: {emp.address}\nAge: {emp.age}\nDesignation: {emp.designation}\nSalary:{emp.salary}")