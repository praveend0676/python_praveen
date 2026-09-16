class BankAccount:
    """
    Represents a bank account.

    Class Variables:
        bank_name: Name of the bank shared by all accounts.
        total_accounts: Total number of accounts created.
    """

    # Class variables
    bank_name = "ABC Bank"
    total_accounts = 0

    def __init__(self, account_holder, account_number, balance=0):
        """
        Initialize a new bank account.
        """

        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

        # Increase account count whenever a new account is created
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        """
        Deposit money into the account.
        """

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount

        print(
            f"₹{amount:.2f} deposited successfully."
        )

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Prevents withdrawal when the amount is greater
        than the available balance.
        """

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount

        print(
            f"₹{amount:.2f} withdrawn successfully."
        )

    def check_balance(self):
        """
        Display the current account balance.
        """

        print(
            f"Current Balance: ₹{self.balance:.2f}"
        )

    def display_account_details(self):
        """
        Display complete account information.
        """

        print("\n--- Account Details ---")
        print(f"Bank Name      : {BankAccount.bank_name}")
        print(f"Account Holder : {self.account_holder}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : ₹{self.balance:.2f}")

    @classmethod
    def change_bank_name(cls, new_name):
        """
        Change the bank name for all accounts.
        """

        if not new_name.strip(): 
            print("Bank name cannot be empty.")
            return

        cls.bank_name = new_name

        print(
            f"Bank name changed to '{new_name}'."
        )

    @classmethod
    def get_total_accounts(cls):
        """
        Return the total number of bank accounts created.
        """

        return cls.total_accounts