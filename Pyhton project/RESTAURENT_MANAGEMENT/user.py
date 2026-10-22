from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Employee(User):
    def __init__(self, name, phone, email, address, age, designation, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employee = [] # eta amader database

    def add_employee(self, restaurant, employee):
        restaurant.add_employee(employee)

    def view_employee(self, restaurant):
        restaurant.view_employee()  # ekhane restaurant ekta object hoye geshe

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_item(item)


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = [] # eta amader database
        self.menu = FoodItem()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
            print("----------------------------------")
            print("Employee List!!")
            for emp in self.employee:
                print(f"Name: {emp.name}\nPhone: {emp.phone}\nEmail: {emp.email}\nAddress: {emp.address}\nAge: {emp.age}\nDesignation: {emp.designation}\nSalary:{emp.salary}")

class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item_name == item:
                return item  # age find korbe then oi item ta pathabe removed othoda cart e add korar jonno
        return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item_name == item:
            self.items.remove(item)
            print('Item deleted')
        else:
            print('Item not found')

    def show_menu(self):
        print('**********MENU**********')
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')

class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


mn = Menu()
item = FoodItem('Pizza', 1200, 10)
mn.add_menu_item(item)
mn.show_menu()