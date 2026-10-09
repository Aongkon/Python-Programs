class shop:
    cart = [] # cart is a class attribute
    def __init__(self, buyer):
        self.buyer = buyer
    def add_to_cart(self, item):
        self.cart.append(item)

aongkon = shop('Aongkon')
aongkon.add_to_cart('shoes')
aongkon.add_to_cart('phone')
# print(aongkon.cart)

nisho = shop('nisho')
nisho.add_to_cart('cap')
nisho.add_to_cart('watch')
# print(nisho.cart)


# output -->
# ['shoes', 'phone']
# ['shoes', 'phone', 'cap', 'watch'] ekhane 2 jonerta ekshathe astese

# /////////////

class shop:
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # cart is an instance attribute
    def add_to_cart(self, item):
        self.cart.append(item)

aongkon = shop('I am aongkon')
aongkon.add_to_cart('longgi')
aongkon.add_to_cart('airbuts')
print(aongkon.cart)

kongkon = shop('I am kongkon')
kongkon.add_to_cart('chironi')
kongkon.add_to_cart('lipstik')
print(kongkon.cart)

# output -->
# ['longgi', 'airbuts']
# ['chironi', 'lipstik']
