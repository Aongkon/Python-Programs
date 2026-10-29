from abc import ABC
from restaurant import Restaurant
class User(ABC):
    def __init__(self, name, phone, gmail, address):
        self.name = name
        self.phone = phone
        self.gmail = gmail
        self.address = address

class Customer(User):
    def __init__(self, name, phone, gmail, address):
        super().__init__(name, phone, gmail, address)
        self.cart = None

    def view_menu(self):
        pass

    def add_to_cart(self):
        pass

    def pay_bill(self, amount):
        pass

class Employee(User):
    def __init__(self, name, phone, gmail, address, age, salary, designation):
        super().__init__(name, phone, gmail, address)
        self.age = age
        self.salary = salary
        self.designation = designation

class Admin(User):
    def __init__(self, name, phone, gmail, address):
        super().__init__(name, phone, gmail, address)

    def add_employee(self, restaurant, ):
        restaurant.add_employees()
    def remove_employee(self):
        pass
    def add_item(self):
        pass
    def remove_item(self):
        pass
    def view_manu(self):
        pass