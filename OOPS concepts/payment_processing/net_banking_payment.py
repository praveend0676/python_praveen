from payment import Payment


class NetBankingPayment(Payment):

    def __init__(self, amount, bank_name):
        super().__init__(amount)
        self.bank_name = bank_name

    def pay(self):
        print(
            f"Processing Net Banking payment "
            f"of ₹{self.amount}"
        )

        print(
            f"Payment successful through "
            f"{self.bank_name}"
        )