# poly ---> many
# morph ---> shape
# ekoy jinish bivhinno rope thakte pare

class Animal:
    def __init__(self, name) -> None:
        self.name = name
    def make_sound(self):  #
        print('Animal making some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):  #
        print('Meow Meow')
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):  #
        print('Ghew Ghew')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):  #
        print('beh beh')


class Less(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):  #
        print('Aw Aw Aw')

don = Cat('Real Don')
don.make_sound()

shepard = Dog('Shephard')
shepard.make_sound()

mess = Goat('LMTen')
mess.make_sound()


less = Less('naymer')
less.make_sound()

animals = [don, shepard, mess, less]
for animal in animals:
    animal.make_sound()