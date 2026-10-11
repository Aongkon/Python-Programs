class Book:
    def __init__(self, name) -> None:
        self.name = name
    def read(self):
        # pass
        raise NotADirectoryError # its showing error 

class Physics(Book):
    def __init__(self, name, lab) -> None:
        self.lab = lab
        super().__init__(name)
    def read(self):  # for that parent method is not going to showing his error
        print('Reading physics vector chapter') 

topon = Physics('Topon', True)
print(issubclass(Physics, Book))
print(isinstance(topon, Physics))
print(isinstance(topon, Book))

topon.read()