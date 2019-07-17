class BankAccount():

    #These are class variables.
    interest_rate = .01
    accounts = []


    def __init__(self):
        self.balance = 0 #This is an instance variable.
        # self.account_name = account_name


    def deposit(self, amount): #This is an instance method.
        self.balance += amount


    def withdraw(self, amount): #This is an instance method.
        self.balance -= amount


    #These are class methods.
    @classmethod
    def create(cls):
        cls.accounts.append(BankAccount())
        return cls()

    @classmethod
    def total_funds(cls):

        for account in cls.accounts:
            print('hey')
        
    





my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
print()

my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
# print(BankAccount.total_funds()) # 1200
print()

# BankAccount.interest_time()
print(my_account.balance) # 202.0
print(your_account.balance) # 1010.0
# print(BankAccount.total_funds()) # 1212.0
print()

my_account.withdraw(50)
print(my_account.balance) # 152.0
# print(BankAccount.total_funds()) # 1162.0