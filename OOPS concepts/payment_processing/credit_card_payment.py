from payment import Payment


class CreditCardPayment(Payment):

    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def pay(self):
        print(
            f"Processing Credit Card payment of ₹{self.amount}"
        )

        print(
            f"Card ending with "
            f"{self.card_number[-4:]} used successfully."
        )