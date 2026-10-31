
class Passenger:
    def __init__(self, bus_number, name, phone, requested_seats):
        self.bus_number = bus_number
        self.name = name
        self.phone = phone
        self.requested_seats = requested_seats

        self.bus = None #  reference to a Bus object // ekhane bus er ekta object asbe

