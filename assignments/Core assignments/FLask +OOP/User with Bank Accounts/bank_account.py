class Bank_account:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0): 
        self.int_rate= int_rate
        self.balance= balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance+=amount
        print(f"added {amount}$ to the balance, the balance will be:{self.balance}")
        return self
        # your code here
    def withdraw(self, amount):
        if(self.balance>=amount):
            self.balance-=amount
            print(f"{amount}$ withdrown from your balnce")
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self
        # your code here
    def display_account_info(self):
        print(f"the account balance is ${self.balance}")
        # your code here
    def yield_interest(self):
        if(self.balance>0):
            self.balance*self.int_rate
        # your code here

bank1= Bank_account(0.02, 600)
bank2=Bank_account(0.01, 900 )
""" bank1.deposit(150).deposit(400).deposit(350).deposit(300)
bank1.withdraw(900)
bank1.display_account_info()
bank1.yield_interest()
print("-"*20)
bank2.deposit(150).deposit(400)
bank2.withdraw(200).withdraw(180).withdraw(200).withdraw(500)
bank2.display_account_info()
bank2.yield_interest() """
class User:
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account = account
    
    # other methods
    def make_deposit(self, amount, account_number):
        self.account[account_number].deposit(amount)
    def make_withdrawal(self, amount,account_number):
        self.account[account_number].withdraw(amount)
    def transfer_money(self, amount, other_user,account_number):
        self.account[account_number].withdraw(amount)
        other_user.account.deposit(amount)