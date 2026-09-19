from user import User
from student import Student
from mentor import Mentor


# ============================================================
# CREATE STUDENT OBJECTS
# ============================================================

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


# ============================================================
# CREATE MENTOR OBJECT
# ============================================================

mentor1 = Mentor(
    "Arun",
    "arun@super30.com",
    "MN101",
    "Python & AI",
    2
)


# ============================================================
# DISPLAY STUDENT INFORMATION
# ============================================================

print("\n" + "=" * 50)
print("STUDENT 1")
print("=" * 50)

student1.display_student_info()


print("\n" + "=" * 50)
print("STUDENT 2")
print("=" * 50)

student2.display_student_info()


# ============================================================
# ASSIGN COURSE
# ============================================================

print("\n" + "=" * 50)
print("COURSE ASSIGNMENT")
print("=" * 50)

student1.assign_course("Advanced Python")


# ============================================================
# SUBMIT ASSIGNMENTS
# ============================================================

print("\n" + "=" * 50)
print("ASSIGNMENTS")
print("=" * 50)

student1.submit_assignment("OOP Assignment")
student1.submit_assignment("Inheritance Assignment")

student2.submit_assignment("Functions Assignment")


# ============================================================
# DISPLAY UPDATED STUDENT
# ============================================================

print("\n" + "=" * 50)
print("UPDATED STUDENT 1")
print("=" * 50)

student1.display_student_info()


# ============================================================
# DISPLAY MENTOR INFORMATION
# ============================================================

print("\n" + "=" * 50)
print("MENTOR INFORMATION")
print("=" * 50)

mentor1.display_mentor_info()


# ============================================================
# ASSIGN STUDENT TO MENTOR
# ============================================================

print("\n" + "=" * 50)
print("ASSIGN STUDENT TO MENTOR")
print("=" * 50)

mentor1.assign_student()


# ============================================================
# DISPLAY UPDATED MENTOR
# ============================================================

print("\n" + "=" * 50)
print("UPDATED MENTOR INFORMATION")
print("=" * 50)

mentor1.display_mentor_info()


# ============================================================
# STATIC METHOD
# ============================================================

print("\n" + "=" * 50)
print("EMAIL VALIDATION")
print("=" * 50)

print(
    "Rahul email valid:",
    User.validate_email("rahul@gmail.com")
)

print(
    "Invalid email:",
    User.validate_email("rahulgmail.com")
)


# ============================================================
# CLASS METHOD
# ============================================================

print("\n" + "=" * 50)
print("TOTAL USERS")
print("=" * 50)

print(
    "Total users created:",
    User.get_total_users()
)
