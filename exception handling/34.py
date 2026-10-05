balance=5000
amount=int(input("Enter amount: "))
if amount > balance:
        raise ValueError("Insufficient balance")
print("Withdrawal successful")
    print(e)