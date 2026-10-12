class Bank:
    def __init__(self, name, balance, add):
        self.name = name
        self.__balance = balance # private
        self._add = add
    def get_balance(self):
        print(self.__balance)

    def __display(self): #private method
        pass

abc = Bank("ABC", 5000, 'Chawrasta')
abc.__balance = 0 # eta alada value hisebe assign hobe
print(abc.__balance) 

abc.get_balance()
print(abc.__balance)
print(abc._add)

print(Bank.__dict__.keys())
