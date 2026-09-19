class User:
    """
    Parent class representing a common user
    in the Super30 Learning Platform.
    """

    # Class variable
    total_users = 0

    def __init__(self, name, email, user_id):
        self.name = name
        self.email = email
        self.user_id = user_id

        # Increase total user count
        User.total_users += 1

    # Instance method
    def display_user_info(self):
        print(f"Name    : {self.name}")
        print(f"Email   : {self.email}")
        print(f"User ID : {self.user_id}")

    # Class method
    @classmethod
    def get_total_users(cls):
        return cls.total_users

    # Static method
    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email
