class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:    #####
            if item_name.lower() == item.name.lower(): # item.name hocche stringta
                return item  # age find korbe then oi item ta pathabe removed othoda cart e add korar jonno
        return None
    
    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item is not None:
            self.items.remove(item)
            print('Item deleted')
        else:
            print('Item not found')

    def show_menu(self):
        print('------------------------------------------------------')
        print('**********MENU**********')
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
