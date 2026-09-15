from Student import Student


# Create student objects
student1 = Student(
    "Rahul",
    "rahul@gmail.com",
    "ST001",
    "Python",
    [85, 90, 78]
)

student2 = Student(
    "Priya",
    "priya@gmail.com",
    "ST002",
    "Data Science",
    [92, 88, 95]
)

student3 = Student(
    "Arjun",
    "arjun@gmail.com",
    "ST003",
    "AI Engineering",
    [75, 82, 80]
)


# Display student details
student1.display_details()
student2.display_details()
student3.display_details()


# Update marks
student1.update_marks([90, 92, 85])

print("\nAfter updating Rahul's marks:")
student1.display_details()


# Display total number of students
print(
    f"\nTotal Students: {Student.get_total_students()}"
)