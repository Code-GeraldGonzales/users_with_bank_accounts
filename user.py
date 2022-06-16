from users_with_bank_accounts import BankAccount

class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = {"checking":BankAccount(int_rate=0.02, balance=0),"savings":BankAccount(int_rate=0.02, balance=500)}

    def make_deposit(self, amount, account_name):
        self.account[account_name].deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self, account_name):
        print(f"Hi {self.first_name} Your Current Balance Is: {self.account[account_name].balance}")
        return self

    def transfer_money(self, amount, other_user,account_name):
        self.account[account_name].balance -= amount
        other_user.account[account_name].balance += amount
        print(f"You Transferred {amount} to {other_user.first_name}!")
        return self

account_holder1 = User("Jerry", "Gonzales", "dude@dude.com", 21)
account_holder2 = User("Alex", "Valdez", "dude@dude.com", 31)


account_holder1.transfer_money(50,account_holder2,"checking")
account_holder2.display_user_balance("checking")


























#  display_info(self) - Have this method print all of the users' details on separate lines.

#     def display_info(self):
#         print(self.first_name, self.last_name)
#         print(f"Email {self.email}")
#         print(f"Is {self.age} years old")
#         print(f"Is {self.is_rewards_member}")
#         print(f"Has {self.gold_card_points} points")
#         return self

# #  enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.

#     def enroll(self):
#         if self.is_rewards_member:
#             print('True is a rewards member')
#         else: 
#             self.is_rewards_member = True
#             self.gold_card_points = 200
#         return self



#     def spend_points(self,amount):
#         if amount > self.gold_card_points:
#             print("You Don't Have Eough Points")
#         else: 
#             self.gold_card_points -= amount
#         return self




# user_1 = User("Jerry", "Gonzales", "dude@dude.com", 53)
# User_2 = User("Armando", "Gonzales", "son@son.com", 24)
# User_3 = User("Caitlyn", "Gonzales", "daughter@daughter.com", 22)
# user_1.display_info().enroll().spend_points(50).display_info()
# User_2.display_info().enroll().spend_points(80)
# User_3.display_info().spend_points(40)