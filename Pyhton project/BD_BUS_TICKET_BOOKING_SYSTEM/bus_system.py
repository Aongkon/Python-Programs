class BusSystem:
    def __init__(self):
         self.buses = []
         self.passengers = []
         self.bus_lookup = {} # dictionary: bus number -> Bus object
         self.is_admin_logged_in = False

    def add_bus(self, bus):
        if not self.is_admin_logged_in:
            print("Access denied! Only admin can add a bus.")
        else:
            if bus.number in self.bus_lookup:
                print(f"Bus number {bus.number} already exists!")
            else:
                self.buses.append(bus)
                self.bus_lookup[bus.number] = bus
                print(f"Bus {bus.number} {bus.route} added successfully with {bus.total_seats} seats.")

    # def show_buses(self):
    #     print(f'Bus Number\tRoute\tTotal Seats\tAvailable Seats')
    #     for bus in self.buses:
    #         print(f"{bus.number} {bus.route} {bus.total_seats} {bus.available_seats()}")

    # def add_passengers(self, passenger):
    #     self.passengers.append(passenger)

    def book_ticket(self, passenger):
        fare = 500
        bus_object = self.bus_lookup.get(passenger.bus_number)

        if bus_object is None:
            print("Bus not found!")
            return
        
        if bus_object.book_seats(passenger.requested_seats):
            self.passengers.append(passenger)
            # print("Ticket booked successfully!")

            print("\n------ TICKET ------")
            print(f"Name   : {passenger.name}")
            print(f"Phone  : {passenger.phone}")
            print(f"Bus No : {bus_object.number}")
            print(f"Route  : {bus_object.route}")
            print(f"Seat No: {bus_object.booked_seats}")
            print(f"Fare   : ৳ {passenger.requested_seats * fare}")
            print("-----------------------")
            print("Ticket booked successfully!")
        else:
            print("Sorry, no seats available on this bus.")

    def show_buses(self):
        if not self.buses: # etar moddhe jdi bus object na thake 
            print("No buses available right now.")
        print("\n--- Available Buses ---")
        for bus in self.buses:
            print(f"Bus No: {bus.number} | Route: {bus.route} | "
                  f"Available Seats: {bus.available_seats()}/{bus.total_seats}")

        
