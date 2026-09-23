from payment import Payment


class UPIPayment(Payment):

    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def pay(self):
        print(
            f"Processing UPI payment of ₹{self.amount}"
        )

        print(
            f"Payment successful using UPI ID: "
            f"{self.upi_id}"
        )