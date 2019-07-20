class BankAccount():

    #These are class variables. They are the same value for all accounts.
    interest_rate = .01
    accounts = []

    def __init__(self, owner_name):
        #These are instance variables. They need to be different from account to account.
        self.owner_name = owner_name 
        self.balance = 0 

    #These are magic methods.
    def __str__(self): #Returns a meaningful string that describes the instance.
        return f'{self.owner_name} bank account: {self.balance}'

    def __repr__(self): #Returns a technical string that describes the instance.
        return f'BankAccount instance:owner_name={self.owner_name} balance={self.balance}'

    #These are instance methods. They pertain to a single, specific account.
    def deposit(self, amount): #Adds the amount to this balance.
        self.balance += amount
        return self.balance

    def withdraw(self, amount): #Subtracts the amount from this balance.
        self.balance -= amount
        return self.balance

    #These are class methods. At the time we run it there is no single, specific account object that we are working on.
    @classmethod
    def create(cls, owner_name): #Instantiates a new BankAccount class and appends it to the accounts list.
        new_account = BankAccount(owner_name)
        cls.accounts.append(new_account)
        return new_account

    @classmethod
    def total_funds(cls): #Returns the sum of all bank_accounts' balances.
        total_sum = 0
        print('\n TOTAL FUNDS:')

        for account in cls.accounts: #Iterates through every account in the accounts list.
            # print(account.balance)
            total_sum += account.balance
                    
        return total_sum
        
    @classmethod
    def interest_time(cls): #Calculates and adds interest to every account based on interest_rate.
        print('\n INTEREST TIME:')
        for account in cls.accounts:
            # print(f'{account.balance} @ {account.interest_rate} = {account.balance * account.interest_rate}')
            account.balance += account.balance * account.interest_rate
        return cls.accounts