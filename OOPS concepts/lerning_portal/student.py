from user import User


class Student(User):
    """
    Student inherits from User.

    This demonstrates hierarchical inheritance
    because Student and Mentor both inherit from User.
    """

    def __init__(self, name, email, user_id, course_name):
        # Call parent class constructor
        super().__init__(name, email, user_id)

        self.course_name = course_name
        self.completed_assignments = []

    # Instance method
    def assign_course(self, course_name):
        self.course_name = course_name

        print(
            f"{self.name} has been assigned to "
            f"the course: {self.course_name}"
        )

    # Instance method
    def submit_assignment(self, assignment_name):
        self.completed_assignments.append(assignment_name)

        print(
            f"{self.name} submitted assignment: "
            f"{assignment_name}"
        )

    # Instance method
    def display_student_info(self):
        self.display_user_info()

        print(f"Course  : {self.course_name}")

        if self.completed_assignments:
            print(
                "Completed Assignments:",
                ", ".join(self.completed_assignments)
            )
        else:
            print("Completed Assignments: None")

