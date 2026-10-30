from abc import ABC

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

    def view_menu(self, restaurant):
        restaurant.show_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)  # jdi find_item e item ta thake tbe shei item return korbe   # just item  eta FoodItem er object

        if item:
            # if item.quantity >= quantity:  
            if quantity > item.quantity:   # ekhane kahini ache thik koralagbo
                print("Item Quantity Exceeded!!")
            else:
                item.quantity = quantity # ey line e jhamela ache thik kora lagbo
                self.cart.add_item(item)
                print('Item added')
        else:
            print("Item not found*")
            
    def view_cart(self):
        print("*******View Cart********")
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items():
            print(f'{item.name} {item.price} {quantity}') # item.name, item.price egola key ba object er man

    def pay_bill(self):
        print(f'Total Price: {self.cart.total_price()}  => Paid Successfully')
        self.cart.clear() # customer tar item golo niye then shegolor bill pay korar por oi cart er to kono proiojon nei shey khetre ekta perticular customer j item niye bill pay korce tar cart clear ba empty kore dew hocche etar maddhome

class Employee(User):
    def __init__(self, name, phone, gmail, address, age, salary, designation):
        super().__init__(name, phone, gmail, address)
        self.age = age
        self.salary = salary
        self.designation = designation

class Admin(User):
    def __init__(self, name, phone, gmail, address):
        super().__init__(name, phone, gmail, address)

    def add_employee(self, restaurant, employee): # restaurant ekta object
        restaurant.add_employees(employee)

    # def remove_employee(self, restaurant, employee): etar proiojon portase na
    #     restaurant.remove_employee(employee)
        
    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self, restaurant, item):
        restaurant.menu.remove_menu_item(item)
    def view_menu(self, restaurant):
        restaurant.show_menu()