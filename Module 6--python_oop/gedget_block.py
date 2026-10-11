class Laptop:
    def __init__(self, brand, model, color, price, memory) -> None:
        self.brand = brand  # common
        self.model = model  # common
        self.color = color  # common
        self.price = price  # common
    def run(self):
        return f'Running laptop: {self.brand}'
    def codding(self):
        return f'Learning python and practicing'

class Phone:
    def __init__(self, brand, model, color, price, dual_sim) -> None:
        self.brand = brand  # common
        self.model = model  # common
        self.color = color  # common
        self.price = price  # common
        self.dual_sim = dual_sim

    def run(self):
        return f'phone tipa tipi kore'

    def phn_call(self, number, text):
        return f'Sending sms to: {self.number} with: {self.text}'

class Camera:
    def __init__(self, brand, model, color, price, pixel):
        self.brand = brand  # common
        self.model = model  # common
        self.color = color  # common
        self.price = price  # common
        self.pixel = pixel
    def change_lens(self):
        pass
    