from user import User
from student import Student
from mentor import Mentor
from admin import Admin


# =====================================================
# CREATE OBJECTS
# =====================================================

student1 = Student(
    "Rahul",
    "rahul@gmail.com",
    "ST101",
    "Python & AI"
)

student2 = Student(
    "Priya",
    "priya@gmail.com",
    "ST102",
    "Data Science"
)

mentor1 = Mentor(
    "Arun",
    "arun@super30.com",
    "MN101",
    "Python & AI"
)

admin1 = Admin(
    "Meena",
    "meena@super30.com",
    "AD101",
    "Learning Operations"
)


# =====================================================
# STUDENT FUNCTIONALITY
# =====================================================

print("\n========== STUDENT ACTIVITIES ==========")

student1.submit_assignment("OOP Assignment")

student1.submit_assignment(
    "Inheritance Assignment"
)

student2.submit_assignment(
    "Functions Assignment"
)

student1.change_course(
    "Advanced Python"
)


# =====================================================
# MENTOR FUNCTIONALITY
# =====================================================

print("\n========== MENTOR ACTIVITIES ==========")

mentor1.assign_student(student1)

mentor1.assign_student(student2)


# =====================================================
# ADMIN FUNCTIONALITY
# =====================================================

print("\n========== ADMIN ACTIVITIES ==========")

admin1.manage_platform(
    "Added a new Python course"
)


# =====================================================
# METHOD OVERRIDING
# =====================================================

print("\n========== METHOD OVERRIDING ==========")

print("\nStudent Information:")
student1.display_info()

print("\nMentor Information:")
mentor1.display_info()

print("\nAdmin Information:")
admin1.display_info()


# =====================================================
# POLYMORPHISM
# =====================================================

print("\n========== POLYMORPHISM ==========")

users = [
    student1,
    student2,
    mentor1,
    admin1
]

for user in users:
    print("\n-----------------------------")

    user.display_info()


# =====================================================
# STATIC METHOD
# =====================================================

print("\n========== STATIC METHOD ==========")

print(
    "Valid Email:",
    User.validate_email("rahul@gmail.com")
)

print(
    "Invalid Email:",
    User.validate_email("rahulgmail.com")
)


# =====================================================
# CLASS METHOD
# =====================================================

print("\n========== CLASS METHOD ==========")

print(
    "Total Users:",
    User.get_total_users()
)