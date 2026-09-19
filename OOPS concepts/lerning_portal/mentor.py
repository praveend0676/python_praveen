from user import User

class Mentor(User):
    """
    Mentor inherits from User.

    This is the second child class in the
    hierarchical inheritance structure.
    """

    def __init__(
        self,
        name,
        email,
        user_id,
        expertise,
        students_assigned=0
    ):
        # Call parent class constructor
        super().__init__(name, email, user_id)

        self.expertise = expertise
        self.students_assigned = students_assigned

    # Instance method
    def assign_student(self):
        self.students_assigned += 1

        print(
            f"Student assigned to mentor {self.name}"
        )

    # Instance method
    def display_mentor_info(self):
        self.display_user_info()

        print(f"Expertise         : {self.expertise}")
        print(
            f"Students Assigned : "
            f"{self.students_assigned}"
        )