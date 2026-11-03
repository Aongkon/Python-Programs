import random

class Bank:
    account_list = []
    loanFacility = True # mane loan newa jabe

    def __init__(self):
        self.name = self.name
        self.total_balance = 10000
        self.total_loan = 0

    def create_account(self, name, email, phone, password):
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
    def declare_bankrupt(self):
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

    def deposit(self, bank, amount):
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

def logged_in_as_user():
    print("f Welcome {user.name} to Standard Bank Your Administrative account No. is {user.account_no}")
    while True:
        print(" __________________________________ ")
        print("| Press 1 for Check Balance.       |")
        print("| Press 2 for Deposit Money.       |")
        print("| Press 3 for Withdraw Money.      |")
        print("| Press 4 for Take loan.           |")
        print("| Press 5 for Transaction History. |")
        print("| Press 6 for logout               |")
        print("|__________________________________|")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            user.show_balance()
        elif choice == 2:
            amount = int(input("Enter the amount you want to deposit : "))
            user.deposit(bank, amount)
        elif choice == 3:
            amount = int(input("Enter the amount you want to withdraw : "))
            user.withdraw(bank, amount)
        elif choice == 4:
            amount = int(input("Enter the amount you want to take loan : "))
            user.take_loan(bank, amount)
        elif choice == 5:
            user.transaction_history()
        elif choice == 6:
             print("Logging out...")
             break
        else:
            print("Invalid Choice.")

def logged_in_as_admin():
    print("f Welcome {user.name} to Standard Bank Your Administrative account No. is {user.account_no}")
    while True:
        print(" _____________________________________________ ")
        print("| Press 1 for Create an user account.         |")
        print("| Press 2 for Delete an user account.         |")
        print("| Press 3 for Show all users.                 |")
        print("| Press 4 for Show total balance of the bank. |")
        print("| Press 5 for Show total loan amount.         |")
        print("| Press 6 for Turn on loan                    |")
        print("| Press 7 for Turn off loan                   |")
        print("| Press 8 for Declare Bankrupt                |")
        print("| Press 9 for Logout                          |")
        print("|_____________________________________________|")

        choice = int(input("Enter your choice : "))

        if choice == 1:
            name = input("Enter name : ")
            email = input("Enter email : ")
            phone = input("Enter phone No : ")
            password = input("Password : ")
            bank.create_account(name, email, phone, password)
        elif choice == 2:
            acnt = int(input("Enter the account you want to delete : "))
            bank.delete_account(acnt)
        elif choice == 3:
            bank.show_users()
        elif choice == 4:
            bank.show_total_balance()
        elif choice == 5:
            bank.show_total_loan
        elif choice == 6:
            bank.loan_on()
        elif choice == 7:
            bank.loan_off
        elif choice == 8:
            bank.declare_bankrupt()
        elif choice == 9:
            print("Logging out...")
            return
        else:
            print("Invalid choice.")

        

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
            print(f'Welcome {name} to Standard Bank Your Administrative account No. is {user.account_no}')
            bank.account_list.append(user)
        else:
            user = Account(name, email, phone, password, 'admin')
            print(f'Welcome {name} to Standard Bank Your Administrative account No. is {user.account_no}')
            bank.account_list.append(user)
    elif op == 'l':
        user_type = input("User/Admin (u/a) : ")
        name = input("Enter your name : ")
        password = input("Enter your password : ")

        for user in bank.account_list:
            if user.name == name:
                if user.password == password:
                    if user_type == 'a':
                        logged_in_as_admin()
                    else:
                        logged_in_as_user()
                else:
                    print("Sorry, Password didn't match. Try again.")
            else:
                print("Sorry, Name didn't match. Try again")