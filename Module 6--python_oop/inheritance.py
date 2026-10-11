class Gadget:  # Base class 
    def __init__(self,brand, model, color, price, made_in):
        self.brand = brand  # common
        self.model = model  # common
        self.color = color  # common
        self.price = price  # common
        self.made_in = made_in  # common
    def run(self):
        return f'phone tipa tipi kore'

class Laptop:
    def __init__(self, memory) -> None:
        self.memory = memory

    def codding(self):
        return f'Learning python and practicing'

class Phone(Gadget):
    def __init__(self, brand, model, price, color, made_in, dual_sim) -> None:
        self.dual_sim = dual_sim
        super().__init__(brand, model, color, price, made_in)
                         
    def __repr__(self):
         return f'Phone: {self.brand} {self.model} {self.price} {self.color}'

    def phn_call(self, number, text):
        return f'Sending sms to: {number} with: {text}'
    
# class Camera:
#     def __init__(self, pixel):
#         self.pixel = pixel
#     def change_lens(self):
#         pass

my_phone = Phone("Samsung", "Galaxy S24", 25000, "Black", "Korea", True)
print(my_phone)