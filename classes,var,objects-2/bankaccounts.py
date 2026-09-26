class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

account1 = BankAccount("Deepika", "1001", 25000)
account2 = BankAccount("Rahul", "1002", 30000)

print(account1.account_holder, account1.account_number, account1.balance)
print(account2.account_holder, account2.account_number, account2.balance)