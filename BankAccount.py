class BankAccount():

    #These are class variables.
    interest_rate = .01
    accounts = []


    def __init__(self, balance=0):
        self.balance = balance #This is an instance variable.
        # self.account_name = account_name


    def deposit(self, amount): #This is an instance method.
        self.balance += amount


    def withdraw(self, amount): #This is an instance method.
        self.balance -= amount


    #These are class methods.
    @classmethod
    def create(cls):
        # cls.accounts.append(BankAccount())

        # BankAccount.accounts.append(BankAccount())


        
        # cls.accounts.append(BankAccount())
        # return BankAccount()
        # return cls()


        new_account = BankAccount()
        cls.accounts.append(new_account)
        return new_account


    @classmethod
    def total_funds(cls):
        our_total = 0
        print('\n TOTAL FUNDS')

        # print(len(cls.accounts)) #2
        # print(cls.accounts[0].interest_rate)


        # for num in range(len(cls.accounts)):
        for num in cls.accounts:
            print(num.balance)
            # print(cls.accounts[num].balance)
            our_total += num.balance
            # pass



            # print(f'--{num}') #0, 1
            # print(cls.accounts[num]) #main BankAccount
            # print(cls.accounts[num])

        # for account in len(cls.accounts):
        #     print(type(cls.accounts[0].balance))        

        # for account in cls.accounts:
            # print(cls.accounts[0].balance)
            # print(account.balance)
            # our_total += cls.accounts[account].balance
            # pass
        
        return our_total
        
    

    # @classmethod
    # def interest_time(cls):
    #     our_total = 0




print('A')
my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
print()


# print(my_account)
# print(your_account)
# print(BankAccount.accounts)

# print(BankAccount.accounts[0].balance)

print('B - Balance Balance Total-Funds')
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
print(BankAccount.total_funds()) # 1200
print()

print('C')
# BankAccount.interest_time()
# print(my_account.balance) # 202.0
# print(your_account.balance) # 1010.0
# print(BankAccount.total_funds()) # 1212.0
print()

print('D')
# my_account.withdraw(50)
# print(my_account.balance) # 152.0
# print(BankAccount.total_funds()) # 1162.0