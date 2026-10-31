class Bus:
    def __init__(self, number, route, total_seats,):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        seats_available = self.total_seats - self.booked_seats
        return seats_available
    
    def book_seat(self, requested_seat):
        if self.available_seats() < requested_seat:
            print(f'No seats here!!')
        else:
            self.booked_seats += requested_seat
            print(f'Seat booked successfully.')


class Passenger:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.bus = None

class BusSystem:
    def __init__(self):
         self.buses = []
         self.passengers = []

    def add_bus(self, bus):
        pass
    def show_buses(self):
        pass
    def book_ticket(self):
        pass

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        pass



bus1 = Bus(1234, 'Gazipur', 30)
bus1.book_seat(28)
bus1.book_seat(3)