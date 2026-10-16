class Shopping:
    cart = [ ] # class attribute ## static attribute
    origin = 'china'

    def __init__(self, name, location) -> None:
        self.name = 'jamuna' # instance attribute
        self.location = 'dhaka'
    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'buying: {item} for price: {price} and remaining: {remaining}' )

    @classmethod
    def hudai_dehi(self, item):
        print('hudai dekhi kinto', item)

    @staticmethod
    def multiply(a, b):
        result = a * b
        print(result)

basundara = Shopping('basun dhara', 'not pop')
basundara.purchase('lungi', 500, 1000)
Shopping.multiply(4, 6)


# static attribute
# static method --> @staticmethod
# class method ---> @classmethod
# difference between class method and static method
