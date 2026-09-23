import sys

from credit_card_payment import CreditCardPayment
from upi_payment import UPIPayment
from net_banking_payment import NetBankingPayment


# Support the rupee (₹) symbol on consoles using legacy encodings
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except AttributeError:
    pass


# Create different payment objects

credit_card = CreditCardPayment(
    2500,
    "1234567812345678"
)

upi = UPIPayment(
    1500,
    "rahul@upi"
)

net_banking = NetBankingPayment(
    5000,
    "State Bank of India"
)


# Store different payment objects
payments = [
    credit_card,
    upi,
    net_banking
]


print("=" * 50)
print("PAYMENT PROCESSING")
print("=" * 50)


# Runtime Polymorphism
for payment in payments:
    payment.pay()
    print("-" * 50)