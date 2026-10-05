class InvalidPaymentError(Exception):
    pass

class Payment:
    def pay(self, amount):
        if amount <= 0:
            raise InvalidPaymentError("Invalid payment amount")
        print("Payment successful")

try:
    p = Payment()
    p.pay(-100)
except InvalidPaymentError as e:
    print(e)