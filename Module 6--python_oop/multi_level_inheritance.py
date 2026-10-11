class Vehicle:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    def rout(self):
        pass
    def __repr__(self) -> str:
        return f'name: {self.name}, price: {self.price}'

class Bus(Vehicle):
    def __init__(self, name, price, seat) -> None:
        self.seat = seat
        super().__init__(name, price) # super dhara parent er init ke bojhay

    def __repr__(self) -> str:
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, name, price, load):
        self.load = load
        super().__init__(name, price)

    def __repr__(self) -> str:
        return super().__repr__()

class PickUpTruck(Truck):
    def __init__(self, name, price, load, weight) -> None:
        self.weight = weight
        super().__init__(name, price, load)

    def __repr__(self) -> str:
        return super().__repr__()

class ACBus(Bus):
    def __init__(self, name, price, seat, temperature) -> None:
        self.temperature = temperature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'{self.seat}, {self.temperature}')
        return super().__repr__()
    

green_line = ACBus('green', 500000, 22, 16)
print(green_line)