from abc import ABC

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()  # cart er maddhome order class er shob kicho ekhn use korte parbo

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            item.quantity = quantity
            self.cart.add_item(item)
            print('Item added')
        else:
            print("Item not found")
    def view_cart(self):
        print("*******View Cart********")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f'{item.name} {item.price} {quantity}')

class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity # jdi cart e item ta already thake
        else:
            self.items[item] = item.quantity # cart e item jdi na thake

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())


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
        self.menu = Menu()

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





mamar_res = Restaurant('Mamar Restaurant')
mn = Menu()
item = FoodItem('Pizza', 12, 10)
item2 = FoodItem('Burger', 10, 30)
admin = Admin('jibon', 'jibon@gmail.com', 125678, 'gazipur dhaka')
admin.add_new_item(mamar_res, item)
admin.add_new_item(mamar_res, item2)
# mn.add_menu_item(item)
# mn.add_menu_item(item2)
# mn.show_menu()

customer1 = Customer('jibon', 'jibon@gmail.com', 125678, 'gazipur dhaka')
# customer1.view_menu(mamar_res)
customer1.view_menu(mamar_res)