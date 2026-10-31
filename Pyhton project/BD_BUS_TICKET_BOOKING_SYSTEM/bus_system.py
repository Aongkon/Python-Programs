class BusSystem:
    def __init__(self):
         self.buses = []
         self.passengers = []
         self.bus_lookup = {} # dictionary: bus number -> Bus object

    def add_bus(self, bus):
        self.buses.append(bus)

    def show_buses(self):
        print(f'Bus Number\tRoute\tTotal Seats\tAvailable Seats')
        for bus in self.buses:
            print(f"{bus.number} {bus.route} {bus.total_seats} {bus.available_seats()}")

    def book_ticket(self, name, phone, bus_number):
        bus_object = self.bus_lookup.get(bus_number)
        if bus_object is None:
            print("Bus not found!")

        if bus_object.book_seats(bus_number):
            print("Ticket booked successfully!")
        else:
            print("Sorry, no seats available on this bus.")

        
