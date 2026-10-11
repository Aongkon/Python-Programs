# from math import pi
class Shape:
    def __init__(self, name) -> None:
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width = width
        super().__init__(name)

    def area(self):   # 
        return self.length * self.width

class Circle(Shape):
    def __init__(self, name, radius, pi) -> None:
        self.radius = radius
        self.pi = pi
        super().__init__(name)

    def area(self):    #
        return self.pi * self.radius * self.radius

rect = Rectangle('rect', 2, 25)
print(rect.area())
cir = Circle('circle', 2, 3.1416)
print(cir.area()) 
