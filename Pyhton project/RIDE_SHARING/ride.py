from datetime import datetime
from vehicle import Car, Bike


class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = [] 
        self.rides = [] # koto golo ride hoise

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    # def add_ride(self, ride):
    #     self.riders.append(ride)

    def __repr__(self):
        return f'Company Name: {self.company_name} with Riders: {len(self.riders)} and Drivers: {len(self.drivers)}'

class Ride:
    def __init__(self, rider, start_location, end_location, vehicle):
        self.rider = rider
        self.driver = None
        self.start_location = start_location
        self.end_location = end_location
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculate_fare(vehicle.vehicle_type)
        self.vehicle = vehicle

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        # ride ses howar por driver ke taka dey so...
        self.rider.wallet -= self.estimated_fare  # estimated_fare mane koto taka taka hoilo
        self.driver.wallet += self.estimated_fare

    # total cost - fare
    # 20 km gechi
    # 1 km = 30 tk
    # 20 --> 20 * 30 = 600
    def calculate_fare(self, vehicle):
        distance = 10 # etar jaygay user theke input newa jete pare j she koto kilo par kortase
        fare_per_km = {
            'car' : 30,
            'bike' : 20,
            'cng' : 25
        }
        return distance * fare_per_km.get(vehicle)

    def __repr__(self):
        return f"Rider Details: Started ride {self.start_location} to {self.end_location}"
        # print(f'Ride Duration: {self.end_time - self.start_time}') repr string dekhay

class RideRequest:  # eykhane j user request korbe tar shokol data thakbe  --> oporer ride class thekey ashbe
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location

class RideMatching:
    def __init__(self, drivers):
        self.available_drivers = drivers # ekhane RideSharing class e driver list k pathacche

    def find_driver(self, ride_request, vehicle_type):
        if len(self.available_drivers) > 0:
            print("Looking for a driver....")
            driver = self.available_drivers[0]

            if vehicle_type == 'car':
                vehicle = Car('car', '9YT53L', 57)
            elif vehicle_type == 'bike':
                vehicle = Bike('bike', '87WE6K', 46)
            ride = Ride(ride_request.rider, ride_request.rider.current_location, ride_request.end_location, vehicle)
 
            driver.accept_ride(ride)
            return ride

    