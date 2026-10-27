from abc import ABC, abstractmethod

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
        self.current_location = current_location  # ekhaane j self.current_location ache eta motolo rider init method er constructor
