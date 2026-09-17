from course import Course, PremiumCourse

# Regular Course
course1 = Course(
    "Python Programming",
    "Rahul Sharma",
    "8 Weeks",
    5000
)

# Regular Course
course2 = Course(
    "Java Programming",
    "Priya Reddy",
    "10 Weeks",
    6000
)

# Premium Courses
premium_course1 = PremiumCourse(
    "Python Full Stack Development",
    "Arjun Kumar",
    "16 Weeks",
    15000,
    "Yes",
    "Yes"
)

premium_course2 = PremiumCourse(
    "Data Science with Python",
    "Sneha Rao",
    "20 Weeks",
    18000,
    "Yes",
    "Yes"
)


# Display course details
course1.show_course_details()
course1.calculate_discount()

course2.show_course_details()
course2.calculate_discount()

premium_course1.show_course_details()
premium_course1.calculate_discount()

premium_course2.show_course_details()
premium_course2.calculate_discount()


# Display total number of courses
print("\n==============================")
print(f"Total Courses Created: {Course.get_course_count()}")
print("==============================")