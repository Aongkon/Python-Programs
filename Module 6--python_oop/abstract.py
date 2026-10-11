from abc import ABC, abstractmethod

class Animal(ABC): # ABC is important
    @abstractmethod
    def eat(self):
        print('I need food')

    @abstractmethod
    def move(self):
        pass
    
class Monkey(Animal):
    def __init__(self, name) -> None:
        self.category = 'Monkey'
        self.name = name
        super().__init__()
        
    def eat(self):
        print('I want banana')

    def move(self):
           print('Hanging on the branches')

layka = Monkey('lucky')
layka.eat()
layka.move()