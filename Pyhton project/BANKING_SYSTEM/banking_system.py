import random

class Bank:
    account_list = []
    loanFacility = True # mane loan newa jabe

    def __init__(self):
        self.name = self.name
        self.total_balance = 10000
        self.total_loan = 0

    def add_account(self, name, email, phone, password):
        pass
    def delete_account(self):
        pass
    def show_users(self):
        pass
    def show_total_balance(self):
        pass
    def show_total_loan(self):
        pass
    def loan_on(self):
        pass
    def loan_off(self):
        pass


class Account:
    def __init__(self, name, email, phone, password, user_type):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.user_type = user_type
        self.account_no = self.generate_account_no()
        self.total_balance = 0
        self.loan_count = 0
        self.transaction_history = []

    def generate_account_no(self):
        new_account_no = random.randint(100000, 199999)
        return new_account_no

    def deposit(self, amount, bank):
        self.total_balance += amount
        bank.total_balance += amount # user taka deposit korle bank er takaw to bare tai

        print(f'\nSuccessfully Deposited {amount}. Your current balance is{self.total_balance}')
        # etaw ekta transaction so etaw transaction history te add korbo
        self.transaction_history.append(f'Deposited {amount} TK')

    def withdraw(self):
        pass

    def show_balance(self):
        pass

    def show_transaction_history(self):
        pass

    def take_loan(self):
        pass


    print("\n\t---Welcome to Standard Bank---\n")
    bank = Bank('Standard Bank')


    while True:
        op = input("Register/Login (r/l) : ")

        if op == 'r':
            user_type = input("User/Admin (u/a) : ")
            name = input("Enter your name : ")
            email = input("Enter your email : ")
            phone = input("Enter your phone no : ")
            password = input("Enter your password : ")

            if user_type == 'u':
                user = Account(name, email, phone, password, 'user')