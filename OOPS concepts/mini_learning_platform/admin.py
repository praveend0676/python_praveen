from user import User


class Admin(User):
    """Admin child class."""

    def __init__(self, name, email, user_id, department):
        super().__init__(name, email, user_id)

        self.department = department

    # Method Overriding
    def display_info(self):
        super().display_info()

        print("Role       : Admin")
        print(f"Department : {self.department}")

    def manage_platform(self, action):
        print(
            f"Admin {self.name} performed: {action}"
        )