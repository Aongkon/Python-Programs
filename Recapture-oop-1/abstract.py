from abc import ABC, abstractmethod
class project(ABC):
    def details(self):
        print("i am aongkon project") # eta hide kortese
    @abstractmethod 
    def security(self):  # abstract main implementation hide kore
        pass
class app(project):
    def security(self):
        print('App security applied')
    def details(self):
        print('i am xyz project')

a = app() # abstract class er object lekha ba define kora jay na
a.details()
a.security()

# ja dekhano proiojon taie dekhai baki shob hide kore 