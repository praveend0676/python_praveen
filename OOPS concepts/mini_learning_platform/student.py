from user import User


class Student(User):
    """Student child class."""

    def __init__(self, name, email, user_id, course):
        super().__init__(name, email, user_id)

        self.course = course
        self.completed_assignments = []

    # Method Overriding
    def display_info(self):
        super().display_info()

        print("Role    : Student")
        print(f"Course  : {self.course}")

        if self.completed_assignments:
            print(
                "Assignments:",
                ", ".join(self.completed_assignments)
            )
        else:
            print("Assignments: None")

    def submit_assignment(self, assignment):
        self.completed_assignments.append(assignment)

        print(
            f"{self.name} submitted: {assignment}"
        )

    def change_course(self, new_course):
        self.course = new_course

        print(
            f"{self.name} changed course to "
            f"{new_course}"
        )