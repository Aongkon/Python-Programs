from abc import ABC, abstractmethod
from ride import RideRequest, RideMatching

class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid) # etar moddhe aro value pathano jabe tar jonno oikhantheke oi value k receive kora lagbe
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        self.initial_amount = initial_amount

    def display_profile(self):
        # return super().display_profile()
        print(f'Rider Name: {self.name} and Email: {self.email}')

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("Amount is less than 0")

    def update_location(self, current_location):
        self.current_location = current_location  # ekhaane ashole location age jeta chilo shetake shodho update kortase karon 1 raider bar bar ashte pare ekta id diye r tar location ek ekbar alada alada hobe 

    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_request = RideRequest(self, destination) # self mane rider class er ekta object ekhane pathacche
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request, vehicle_type)
        self.current_ride = ride
        print("YAY!! We got a Ride.")

    def show_current_ride(self):
        print(self.current_ride)


class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.wallet = 0
        self.current_location = current_location

    def display_profile(self):
        print(f"Driver Name: {self.name}")

    def accept_ride(self, ride):
        # accept korbo
        ride.start_ride()
        ride.set_driver(self) # driver er object dibo ----> self tai oi Driver class er ekta object ke mean kortase. jokhon self k pass korbo tokho driver class er object chole jabe
    def reach_destination(self, ride):
        ride.end_ride()
