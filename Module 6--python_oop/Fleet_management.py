class Company:
    def __init__(self, name, address) -> None:
        self.name = name
        self.driver = []
        self.buss = []
        self.counter = []
        self.route = []
        self.manager = []
        self.supervisor = []
        pass

class Driver:
    def __init__(self, name, age, home, license) -> None:
        self.name = name
        self.age = age
        self.home = home
        self.license = license
        pass

class Buses:
    def __init__(self, fit, number, paper) -> None:
        self.fit = fit
        self.number = number
        self.paper = paper
        pass

class Counter: 
    def __init__(self) -> None:
        pass
    def purchase_a_ticket(self, start, end, ac, noneac, fare):
        pass

class Passenger:
    def __init__(self) -> None:
        pass

class Supervisor:
    def __init__(self) -> None:
        pass

class Route:
    def __init__(self):
        pass