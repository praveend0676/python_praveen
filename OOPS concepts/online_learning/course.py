class Course:
    course_count = 0

    def __init__(self, course_name, instructor, duration, price):
        self.course_name = course_name
        self.instructor = instructor
        self.duration = duration
        self.price = price

        Course.course_count += 1

    def show_course_details(self):
        print("\n------ Course Details ------")
        print(f"Course Name : {self.course_name}")
        print(f"Instructor  : {self.instructor}")
        print(f"Duration    : {self.duration}")
        print(f"Price       : ₹{self.price:,.2f}")

    def calculate_discount(self):
        discount = self.price * 0.10
        final_price = self.price - discount

        print(f"Discount    : ₹{discount:,.2f}")
        print(f"Final Price : ₹{final_price:,.2f}")

        return final_price

    @classmethod
    def get_course_count(cls):
        return cls.course_count


class PremiumCourse(Course):

    def __init__(
        self,
        course_name,
        instructor,
        duration,
        price,
        mentor_support,
        live_sessions
    ):
        super().__init__(
            course_name,
            instructor,
            duration,
            price
        )

        self.mentor_support = mentor_support
        self.live_sessions = live_sessions

    def show_course_details(self):
        super().show_course_details()

        print(f"Mentor Support : {self.mentor_support}")
        print(f"Live Sessions  : {self.live_sessions}")

    def calculate_discount(self):
        discount = self.price * 0.20
        final_price = self.price - discount

        print(f"Premium Discount : ₹{discount:,.2f}")
        print(f"Final Price      : ₹{final_price:,.2f}")

        return final_price