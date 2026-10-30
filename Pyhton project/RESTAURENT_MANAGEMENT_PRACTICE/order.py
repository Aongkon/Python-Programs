class Order:
    def __init__(self):
        self.items = {} # eta ashole customer er jonno dictionary

    def add_item(self, item):
        if item in self.items:
            self.items[item] += item.quantity # customer lite 2 tar order korce then eki food aro 3 ta order korce tokhon quantity bere jabe. karon dictionary ta customer er jonno
        else:
            self.items[item] = item.quantity

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        # sum = 0
        # for item, quantity in self.items.items():
        #     sum = item.price * quantity
        # return sum

        # same
        return sum(item.price * quantity for item, quantity in self.items.items())
    def clear(self):
        self.items = {} # ete items empty hoia jay


    
    