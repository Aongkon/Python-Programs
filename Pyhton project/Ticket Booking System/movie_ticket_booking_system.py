class Hall:
    def __init__(self, hall_no, row, col):
        self.hall_no = hall_no
        self.row = row
        self.col = col
        self.seats = {} # dictionary
        self.show_list = []

    def enter_show(self, show_id, movie_name, time):
        self.tuple = (show_id, movie_name, time)
        self.show_list.append(self.tuple)
        self.seat_list = []
        for i in range(self.row): # 6 ta row
            row = []
            for j in range(self.col): # 8 ta col
                row.append('Free')
            self.seat_list.append(row)
        self.seats[show_id] = self.seat_list

    def view_show_list(self):
        for x in self.show_list:
            print(f'Show id: {x[0]}\t Movie: {x[1]}\t Time: {x[2]}')

    def view_available_seats(self, id):
        if id not in self.seats:
            print('wrong show id')
        else:
            print("\n-------------------------------------------------\n")
            for i in self.show_list:
                if i[0] == id:
                    print(f'Movie: {i[1]} \t\t Time: Today at {i[2]}\n')
            for x in range(self.row):
                for y in range(self.col):
                    if self.seats[id][x][y] == 'Free':
                        # print('Free', end='\t')
                        print(f"{chr(x+65)}{y+1}", end='\t')
                    else:
                        print('X', end='\t')
                    # print(self.seats[id][x][y], end=' ')  # id ta holo key
                print('\n')

# eta main logic
    def book_tickets(self, id, name, phone, booking_seats):
        flag = 0
        self.booked_tickets = []
        for x in booking_seats:
            r = ord(x[0])-65 # character k integer e anar jonno ord use kore
            c = ord(x[1])-49
            # print(r,c)
            if r >= self.row or c >= self.row or r < 0 or c < 0:
                print("Seat doesn't exists")
            elif self.seats[id][r][c] != 'Free':
                print(x,"is already booked")
            else:
                self.seats[id][r][c] = 'x'
                self.booked_tickets.append(x)
                flag = 1

        if flag == 1:
            print('\n\t ##### Ticket booked successfully #####')
            print("\n-------------------------------------------------\n")
            print('Name: ', name)
            print('Phone: ', phone)
            for i in self.show_list:
                if i[0] == id:
                    print(f'Movie: {i[1]} Time: Today at {i[2]}')
            print('Tickets: ', end=' ')
            for i in self.booked_tickets:
                print(i, end=' ')
            print(f'\nHall no: {self.hall_no}')
            print('Price: ', 500*len(self.booked_tickets), 'TK')


my_hall = Hall(2, 6, 8)
my_hall.enter_show(147, 'Dom', '10:00am')
my_hall.enter_show(205,'Bonolota Express','01:00 PM')
my_hall.enter_show(241,'Rakkhosh','04:00 PM')
my_hall.enter_show(334,'Pressure Cooker','09:00 PM')



while True:
    print("\n-------------------------------------------------\n")
    print("1. View all show today")
    print("2. View available seats")
    print("3. Book tickets")

    option = int(input("Enter your option: "))

    if option == 1:
        print("\n-------------------------------------------------\n")
        my_hall.view_show_list()

    elif option == 2:
        id = int(input('Enter show id: '))
        my_hall.view_available_seats(id)
        
    elif option == 3:
        id = int(input('Enter show id: '))
        name = input('Enter your name: ')
        phone = input('Enter your phone no: ')
        tickets = int(input('Enter number of tickets: '))
        booking_seats = []
        for i in range(tickets):
            booking_seats.append(input('Enter your seat number: '))

        my_hall.book_tickets(id, name, phone, booking_seats)
    else:
        print("Wrong option. Choose again.")
