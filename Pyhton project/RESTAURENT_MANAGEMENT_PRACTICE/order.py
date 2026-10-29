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

    
    