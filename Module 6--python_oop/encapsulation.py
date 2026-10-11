class Bank:
    def __init__(self, holder_name, initial_balance) -> None:
        self.holder_name = holder_name # public attribute
        self._branch = 'Banani 11' # protected attribute
        self.__balance = initial_balance # privet attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            print(f'You have enough money') 
    
rafsan = Bank("Rafsan", 100000)
rafsan.holder_name = 'choto vhai' # holder name ekti constructor tai '=' diye value dite hoy
rafsan.deposit(50000)
# print(rafsan)
print(rafsan.holder_name)
print(rafsan.get_balance()) # method
print(rafsan._branch)
print(rafsan.withdraw(50000))

# print(rafsan.__balance) # privet attribute 
# print(dir(rafsan)) # eta ude kore privet value dekha jay
print(rafsan._Bank__balance) # eta ude kore privet value dekha jay