from bank_account import BankAccount


def main():
    print("===================================")
    print("     BANKING MANAGEMENT SYSTEM")
    print("===================================")

    # Create first bank account
    account1 = BankAccount(
        "Rahul",
        "ACC001",
        10000
    )

    # Create second bank account
    account2 = BankAccount(
        "Priya",
        "ACC002",
        25000
    )

    # Create third bank account
    account3 = BankAccount(
        "Arjun",
        "ACC003",
        15000
    )

    # --------------------------------
    # Display account details
    # --------------------------------

    print("\n1. ACCOUNT DETAILS")

    account1.display_account_details()
    account2.display_account_details()
    account3.display_account_details()

    # --------------------------------
    # Deposit
    # --------------------------------

    print("\n2. DEPOSIT")

    account1.deposit(5000)

    account1.check_balance()

    # --------------------------------
    # Withdraw
    # --------------------------------

    print("\n3. WITHDRAW")

    account1.withdraw(3000)

    account1.check_balance()

    # --------------------------------
    # Test insufficient balance
    # --------------------------------

    print("\n4. WITHDRAW VALIDATION")

    account1.withdraw(20000)

    account1.check_balance()

    # --------------------------------
    # Change bank name
    # --------------------------------

    print("\n5. CHANGE BANK NAME")

    BankAccount.change_bank_name(
        "Global Bank"
    )

    # Display details again
    print("\nUpdated Account Details:")

    account1.display_account_details()
    account2.display_account_details()
    account3.display_account_details()

    # --------------------------------
    # Total number of accounts
    # --------------------------------

    print("\n6. TOTAL ACCOUNTS")

    total = BankAccount.get_total_accounts()

    print(
        f"Total Bank Accounts: {total}"
    )


if __name__ == "__main__":
    main()