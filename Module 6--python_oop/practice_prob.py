class Product:
    def __init__(self) -> None:
        self.products = []

class Shop(Product):
    def __init__(self):
        super().__init__()
    def add_product(self, product_name):
        # self.product_name = product_name
        self.products.append(product_name)
        return f'{product_name}'
    def buy_products(self, selling_product):
        found = False
        for p in self.products:
            if p == selling_product:
                # print(f'Yes, This product is available. You can purchase it.')
                found = True
                # return
            # else:
            #     print(f'No, Its not available')
        if found:
            print(f'Yes, This product is available. You can purchase it.')
        else:
            print(f'No, Its not available')
        

product_name = Shop() 

# product_name.buy_products("tea") # for the first as add_product have not any products

product_name.add_product("milk")
product_name.add_product("egg")
product_name.add_product("tea")
product_name.add_product("chicken")
# product_name.buy_products("tea")
product_name.buy_products("rice")
# print(product_name.add_product())