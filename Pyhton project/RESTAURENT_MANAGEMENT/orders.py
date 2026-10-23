class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity # jdi cart e item ta already thake
        else:
            self.items[item] = item.quantity # cart e item jdi na thake

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    @property # eta ekta variable hoye geche ekhn
    def total_price(self):
        return sum(item.price * quantity for item, quantity in self.items.items())
    def clear(self):
        self.items = {}

