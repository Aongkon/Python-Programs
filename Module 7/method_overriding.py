class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat managso poraw')
    def exercise(self):
        raise NotImplementedError
class Cricket(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)

        ### method override 
    def eat(self):
        print('vegetables')
    def exercise(self):
        print('gym is good for our body')

sakib = Cricket('sakib', 38, 68, 91, 'bd')
sakib.eat()
sakib.exercise()