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
        if requested_seat <= 0:
            # print(f'No seats available!!')
            return False
        elif self.available_seats() < requested_seat:
            # print(f'Request Rejected!!')
            return False
        else:
            self.booked_seats += requested_seat
            # print(f'Seat booked successfully.')
            return True



bus1 = Bus(1234, 'Gazipur', 30)
bus1.book_seat(28)
bus1.book_seat(3)
print(bus1.available_seats())