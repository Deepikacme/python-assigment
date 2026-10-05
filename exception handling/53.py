def withdraw(balance, amount):
        if amount > balance:
            raise ValueError("Insufficient balance")

        print("Withdrawal successful")
print(not withdraw(5000,6000))
withdraw(5000, 6000)