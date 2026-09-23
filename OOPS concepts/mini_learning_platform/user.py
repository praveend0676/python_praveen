class User:
    """Parent class for all users."""

    total_users = 0

    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

        User.total_users += 1

    def display_info(self):
        print(f"Name    : {self.name}")
        print(f"Email   : {self.email}")
        print(f"User ID : {self.user_id}")
        print("Role    : User")

    @classmethod
    def get_total_users(cls):
        return cls.total_users

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email