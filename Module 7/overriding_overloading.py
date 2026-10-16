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

    ## Operator Overloading
    def __add__(self, other):
        return self.age + self.age
    def __mul__(self, other):
        return self.weight * self.weight



sakib = Cricket('sakib', 38, 68, 91, 'bd')
mushfik = Cricket('mushfik', 56, 28, 45, 'bd')
sakib.eat()
sakib.exercise()


## Operator Overloading
print(45 + 63)
print('sakib' + 'rakib')
print([12, 98] + [5, 6, 7, 1, 2])
# print(sakib > mushfik)
# print(len(sakib))