from abc import ABC, abstractmethod


class Payment(ABC):
    """
    Abstract parent class for payment processing.
    """

    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self):
        """
        Every payment type must implement pay().
        """
        pass