class InvalidTransactionError(Exception):
    pass

try:
    amount = int(input("Enter transaction amount: "))

    if amount <= 0:
        raise InvalidTransactionError("Invalid transaction")

    print("Transaction successful")

except InvalidTransactionError as e:
    print(e)