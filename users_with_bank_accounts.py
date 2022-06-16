class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance): 

        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)


    def deposit(self, amount):
        self.balance += amount
        print(f"Your Deposit Is {amount}")
        return(self)

    
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        else: 
            self.balance -= amount
        return self


    def display_account_info(self):
        print(f"Your Balance Is $ {self.balance}")
        return self


    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("You Have zero funds")
        return self

    @classmethod
    def all_accounts_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()
                
        

new_account = BankAccount(.1, 500)
new_account2 = BankAccount(.1, 250)
new_account.deposit(25).deposit(25).deposit(25).withdraw(10).yield_interest().display_account_info()
new_account2.deposit(10).deposit(15).withdraw(2).withdraw(10).withdraw(10).withdraw(10).yield_interest().display_account_info()
BankAccount.all_accounts_info()
