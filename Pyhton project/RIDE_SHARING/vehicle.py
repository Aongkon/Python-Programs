from abc import ABC

class Vehicle(ABC):

    speed = {  # eta class variable eta shob jaygay use kora jabe 
        "car" : 50,
        "bike" : 60,
        "cng" : 70,
    }

    def __init__(self, vehicle_type, vehicle_plate, rate):
        self.vehicle_type = vehicle_type
        self.vehicle_plate = vehicle_plate
        self.rate = rate

class Car(Vehicle):
    def __init__(self, vehicle_type, vehicle_plate, rate):
        super().__init__(vehicle_type, vehicle_plate, rate)

class Bike(Vehicle):
    def __init__(self, vehicle_type, vehicle_plate, rate):
        super().__init__(vehicle_type, vehicle_plate, rate)