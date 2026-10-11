class Family:
    def __init__(self, address) -> None:
        self.address = address
        # return f'the add is: {address}'  eta projojjo noy __init__ methon attribute shongrokkhon kore

class School:
    def __init__(self, id, level) -> None:
        self.id = id
        self.level = level

class Sports:
    def __init__(self, game) -> None:
        self.game = game

class Student(Family, School, Sports):
    def __init__(self, address, id, level, game) -> None:
        School.__init__(self, id, level)
        Sports.__init__(self, game)
        super().__init__(address)
        Family.__init__(self, address)

    def __repr__(self) -> str:
        return (
            f'Address: {self.address}\n'
            f'ID: {self.id}\n'
            f'Level: {self.level}\n'
            f'Game Name: {self.game}'
        )

# my_family = Family('Dighirchala')
student1 = Student("Dighirchala", 101, 12, "Football")
print(student1)