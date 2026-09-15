class Student:
    # Class variable
    total_students = 0

    def __init__(self, name, email, student_id, course, marks):
        self.name = name
        self.email = email
        self.student_id = student_id
        self.course = course
        self.marks = marks

        # Increment total students whenever an object is created
        Student.total_students += 1

    # Instance method
    def display_details(self):
        print("\n--- Student Details ---")
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Email      : {self.email}")
        print(f"Course     : {self.course}")
        print(f"Marks      : {self.marks}")
        print(f"Average    : {self.calculate_average():.2f}")

    # Instance method
    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"Marks updated successfully for {self.name}.")

    # Instance method
    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    # Class method
    @classmethod
    def get_total_students(cls):
        return cls.total_students