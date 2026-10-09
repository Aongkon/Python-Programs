class shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)
    def remove_item(self, item):
        pass
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            # print(item)
            total += item['price'] * item['quantity']
        print('total price', total)
        if amount < total:
            print(f'please provide { total - amount} money')
        else:
            extra = amount - total
            print(f'here is your items and extra money {extra}')
aongkon = shopping('aongkon')
aongkon.add_to_cart('alu', 50, 6)
aongkon.add_to_cart('dim', 70, 12)
print(aongkon.cart)
# aongkon.checkout(600)
aongkon.checkout(1200)