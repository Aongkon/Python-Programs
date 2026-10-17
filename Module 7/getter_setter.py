# Read Only --> you can not be set value. value can not be changed
# Getter --> get a value of a property through a method. Most of the time, you will get the value of a privet attribute
# Setter --> set a value of a property through a method. Most of the time, you will set the value of a privet attribute


class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self.__money = money

    # getattr without any setter is readonly attribute
    @property  # jdi ey method ke property hishebe use kora lage then @property likhley hobe
    def age(self):
        return self._age
    
    @property
    def salary(self):
        return self.__money

    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            return 'salary can not be negative' 
        else:
            self.__money += value

    


samsu = User('samsu', 24, 3000)

# print(samsu.__money) # eta kaj korbe na
# print(samsu.age()) # eta method hishebe kaj kore
print(samsu.age) # eta property hishebe kaj kore
# print(samsu.salary()) #property call kore method define korle error ashbe
print(samsu.salary) 
# samsu.salary(2000) # eta method na tai evhabe dile error ashbe 
samsu.salary = 2000
print(samsu.salary)