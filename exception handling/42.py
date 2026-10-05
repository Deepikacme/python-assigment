class InsufficientBalanceError(Exception):
    pass
    balance=5000
    amount=int(input("Enter amount: "))

    if amount>balance:
        raise InsufficientBalanceError("Insufficient balance")
print("Withdrawal successful")
print(e)