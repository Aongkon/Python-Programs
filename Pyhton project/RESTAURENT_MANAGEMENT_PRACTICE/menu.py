class Menu:
    def __init__(self):
        self.items = []

    def add_menu_item(self, item):
        self.item.append(item) # item ta ekta hocche FoodItem class er object

    def find_item(self, item_name):
        for item in self.items:
            if item == item_name:
                return item
        return None # jdi item pawa na jay tbe none return korbe
    
    def remove_menu_item(self, item_name):
        item = self.find_item(item_name)  # ekhane self ta ashone Menu er ekta object hisebe kaj kortese
        if item is not None:
            self.items.remove(item)
            print(f"{item} deleted")
        else:
            print(f'{item} is not found!')

    def show_menu(self):
        print('------------------------------------------------------')
        print('**********MENU**********')
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"Item Name: {item.name}\tPrice: {item.price}\t Quantity: {item.quantity}")
    