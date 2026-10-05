class InsufficientBalanceError(Exception):
    pass
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
            if amount > self.balance:
                raise InsufficientBalanceError("Insufficient balance")
            self.balance-=amount
            print("Withdrawal successful")
            print("remaining blance:",self.balance)
account=InsufficientBalanceError(5000)
account.withdraw(6000)