from admin import Admin, AdminMenu
from bus_system import BusSystem
from passenger import Passenger


admin = Admin("aongkon_07", "605@#jm7")
system = BusSystem()

while True:
    print("\n========== Bangladesh Bus Ticket Booking System ==========")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        user_name = input("Enter your user name: ")
        password = input("Enter your password: ")

        if admin.login(user_name, password): # eta admin e gele sekhan theke ekta value asbe
            system.is_admin_logged_in = True
            print("Login successful! Welcome, admin.")
            admin_menu = AdminMenu()  # eyjaygay bojte  kosto hoia gese************ ey toko beshi moja lagse
            admin_menu.show_admin_menu(system)

        else:
            print("Wrong username or password!")
    elif choice == '2':
        system.show_buses()
        if system.buses: # jdi bus object na thake
            bus_number = int(input("Enter bus number: "))
            name = input("Your name: ")
            phone = int(input("Phone number: "))
            requested_seats = int(input("Requested Seats: "))

            passenger = Passenger(bus_number=bus_number, name=name, phone=phone, requested_seats=requested_seats)
            system.add_passengers(passenger)

    elif choice == '3':
        system.show_buses()
    elif choice == '4':
        print("Thank you for using the system. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3 or 4.")



