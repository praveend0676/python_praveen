from calculator import add
from student import Student
from employee import Employee


print("=== Calculator ===")
print("10 + 20 =", add(10, 20))

print("\n=== Student ===")

student = Student("Rahul", 85)
student.display()

print("\n=== Employee ===")

employee = Employee(
    "EMP101",
    "Praveen",
    75000
)

employee.display()