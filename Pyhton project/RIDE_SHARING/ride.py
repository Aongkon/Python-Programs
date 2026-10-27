from datetime import datetime

class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = [] 
        self.rides = [] # koto golo ride hoise

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.riders.append(driver)

    # def add_ride(self, ride):
    #     self.riders.append(ride)

    def __repr__(self):
        return f'Company Name: {self.company_name} with Riders: {len(self.riders)} and Drivers: {len(self.drivers)}'

class Ride:
    def __init__(self, start_location, end_location):
        self.start_location = start_location
        self.end_location = end_location
        self.driver_name = None
        self.rider_name = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = None

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        # ride ses howar por driver ke taka dey so...
        self.rider_name.wallet -= self.estimated_fare  # estimated_fare mane koto taka taka hoilo
        self.driver_name.wallet += self.estimated_fare

    def __repr__(self):
        return f"Rider Details: Started ride {self.start_location} to {self.end_location}"
        # print(f'Ride Duration: {self.end_time - self.start_time}') repr string dekhay

class RideRequest:  # eykhane j user request korbe tar shokol data thakbe  --> oporer ride class thekey ashbe
    def __init__(self,rider, end_location):
        self.rider = rider
        self.end_location = end_location

class RideMatching:
    def __init__(self, drivers):
        self.available_drivers = drivers

    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            print("Looking for a driver....")
            driver = self.available_drivers[0]
            ride = Ride(ride_request.rider.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride

    