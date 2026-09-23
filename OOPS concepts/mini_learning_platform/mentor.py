from user import User


class Mentor(User):
    """Mentor child class."""

    def __init__(self, name, email, user_id, expertise):
        super().__init__(name, email, user_id)

        self.expertise = expertise
        self.students_assigned = []

    # Method Overriding
    def display_info(self):
        super().display_info()

        print("Role      : Mentor")
        print(f"Expertise : {self.expertise}")
        print(
            f"Students Assigned : "
            f"{len(self.students_assigned)}"
        )

    def assign_student(self, student):
        self.students_assigned.append(student)

        print(
            f"{student.name} assigned to "
            f"mentor {self.name}"
        )