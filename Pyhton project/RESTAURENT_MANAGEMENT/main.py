from food_item import FoodItem
from menu import Menu
from orders import Order
from restaurant import Restaurant
from user import Customer, Employee, Admin

mamar_restaurant = Restaurant("Mamar Restaurant")
def customer_menu():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    address = input('Enter your address: ')
    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {customer.name}!!")
        print(f"1. View menu")
        print(f"2. Add item to cart")
        print(f"3. View Cart")
        print(f"4. PayBill")
        print(f"5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            customer.view_menu(mamar_restaurant)
        elif choice == 2:
            item_name = input('Enter item name: ')
            item_quantity = int(input('Enter item quantity: '))
            customer.add_to_cart(mamar_restaurant, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print('Invalid Input')



def admin_menu():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    address = input('Enter your address: ')
    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f"Welcome {admin.name}!!")
        print(f"1. Add new item")
        print(f"2. Add new employee")
        print(f"3. View Employee")
        print(f"4. View items")
        print(f"5. Delete item")
        print(f"6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = FoodItem(item_name, item_quantity, item_price)
            admin.add_new_item(mamar_restaurant, item)
        elif choice == 2:
            name = input('Enter employee name: ')
            phone = int(input('Enter employee phone No.: '))
            email = input('Enter employee email: ')
            address = input('Enter employee name: ')
            designation = input('Enter employee designation: ')
            age = input('Enter employee age: ')
            salary = input('Enter employee salary: ')

            admin.add_employee(name, phone, email, address, 
                               age, designation, salary)
        elif choice == 3:
            admin.view_employee(mamar_restaurant)
        elif choice == 4:
            admin.view_menu(mamar_restaurant)
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(mamar_restaurant, item_name)
        elif choice == 6:
            break
        else:
            print('Invalid Input')

