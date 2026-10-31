from bus import Bus
# from bus_system import BusSystem


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            return True
        else:
            # return f"User Invalid!!"
            return False

class AdminMenu():
        # def __init__(self):
        #     self.system = BusSystem()

        def show_admin_menu(self, system):
            while system.is_admin_logged_in:
                print("\n=== Admin Menu ===")
                print("1. Add Buses")
                print("2. View All Buses")
                print("3. Logged Out")
                choice = input("Enter your choice: ")
                if choice == '1':
                    number = int(input("Enter the bus number: "))
                    route = input("Enter the bus route name: ")
                    total_seats = int(input("Enter total seats count: "))
                    bus = Bus(number=number, route=route, total_seats=total_seats)
                    system.add_bus(bus)
                elif choice == '2':
                    system.show_buses()
                elif choice == '3':
                    # self.system.is_admin_logged_in = False
                    system.is_admin_logged_in = False
                    print("Logged Out Successfully.")
                else:
                    print("Invalid choice! Please enter 1, 2 or 3.")
                    
        


