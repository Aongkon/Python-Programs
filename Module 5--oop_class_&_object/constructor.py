class phone:
    #attributes

# eta vhitorer shokol parameter phone class er under e r init holo constructor
    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price
My_phone = phone('kala chan', 'oppo', 9800)
# print(My_phone.owner, My_phone.price)



#new 
class pen:
    # attributes here

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

shomas_pen = pen('matador', 'red', 10)
romons_pen = pen('good luck', 'blue', 15)
my_pen = pen('jhakastro', 'yellow', 25)

all_here = [shomas_pen, romons_pen, my_pen]
for value in all_here:
    print(f'{value.name} {value.price} {value.color}')
    