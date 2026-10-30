from food_item import FoodItem
from menu import Menu
from orders import Order
from restaurant import Restaurant
from user import Customer, Employee, Admin

mamar_restaurant = Restaurant("Mamar Restaurant")
def customer_menu():
    print('------------------------------------------------------')
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    address = input('Enter your address: ')
    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print('------------------------------------------------------')
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
    print('------------------------------------------------------')
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone: ')
    address = input('Enter your address: ')
    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print('------------------------------------------------------')
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
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_restaurant, item)
        elif choice == 2:
            name = input('Enter employee name: ')
            phone = int(input('Enter employee phone No.: '))
            email = input('Enter employee email: ')
            address = input('Enter employee address: ')
            designation = input('Enter employee designation: ')
            age = input('Enter employee age: ')
            salary = input('Enter employee salary: ')
            employee = Employee(name, phone, email, address, age, designation, salary)
            admin.add_employee(mamar_restaurant, employee)

        elif choice == 3:
            print("Choice 3 selected!")
            admin.view_employee(mamar_restaurant)
            print("Employee function finished!")
        elif choice == 4:
            admin.view_menu(mamar_restaurant)
        elif choice == 5:
            item_name = input("Enter item name: ")
            admin.remove_item(mamar_restaurant, item_name)
        elif choice == 6:
            break
        else:
            print('Invalid Input')

while True:
    print('------------------------------------------------------')
    print("Welcome!!")
    print("1.Customer Site")
    print("2.Admin Panel")
    print("3.Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input")

