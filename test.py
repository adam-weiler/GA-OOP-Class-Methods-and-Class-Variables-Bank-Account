from BankAccount import BankAccount

my_account = BankAccount.create('Jim')
your_account = BankAccount.create('Spock')
print(f'{my_account.owner_name}\'s BALANCE: {my_account.balance}') # 0

print(f'{BankAccount.total_funds()} \n') # 0

print(f'{my_account.owner_name}\'s DEPOSIT: {my_account.deposit(200)}')
print(f'{your_account.owner_name}\'s DEPOSIT: {your_account.deposit(1000)}')
print(f'{my_account.owner_name}\'s BALANCE: {my_account.balance}') # 200
print(f'{your_account.owner_name}\'s BALANCE: {your_account.balance}') # 1000

print(f'{BankAccount.total_funds()} \n') # 1200

BankAccount.interest_time()
print(f'{my_account.owner_name}\'s BALANCE: {my_account.balance}') # 202.0
print(f'{your_account.owner_name}\'s BALANCE: {your_account.balance}') # 1010.0

print(f'{BankAccount.total_funds()} \n') # 1212.0

my_account.withdraw(50)
print(f'{my_account.owner_name}\'s BALANCE: {my_account.balance}') # 152.0

print(f'{BankAccount.total_funds()} \n') # 1162.0