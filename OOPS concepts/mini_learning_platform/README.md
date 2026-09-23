# 🎓 Mini Learning Platform — Inheritance & Method Overriding

## 📌 Project Overview

Design and build a small **Learning Platform** using Python Object-Oriented Programming (OOP).

The application models different types of users:

- **Student**
- **Mentor**
- **Admin**

A common parent class called `User` contains properties and functionality shared by all users. Each child class adds its own role-specific functionality.

This project demonstrates **Inheritance, Hierarchical Inheritance, Method Overriding, `super()`, and Polymorphism**.

---

## 🎯 Problem Statement

Create a parent `User` class and child classes such as:

```text
                         User
              ___________|___________
             /           |           \
        Student        Mentor        Admin
```

### User

The `User` class should contain common properties:

- Name
- Email
- User ID

### Student

The `Student` class should inherit from `User` and contain:

- Course
- Completed Assignments

Student functionality:

- Submit an assignment
- Change course
- Display student information

### Mentor

The `Mentor` class should inherit from `User` and contain:

- Expertise
- Assigned students

Mentor functionality:

- Assign a student
- Display mentor information

### Admin

The `Admin` class should inherit from `User` and contain:

- Department

Admin functionality:

- Manage the learning platform
- Display admin information

---

## 🌳 Inheritance Used

This project uses **Hierarchical Inheritance**.

```text
                         User
              ___________|___________
             /           |           \
        Student        Mentor        Admin
```

### Definition

> **One parent class + multiple child classes = Hierarchical Inheritance**

All three child classes inherit common functionality from `User`.

---

## 🔄 Method Overriding

The parent `User` class defines:

```python
def display_info(self):
    ...
```

Each child class provides its own implementation:

```python
class Student(User):

    def display_info(self):
        ...
```

```python
class Mentor(User):

    def display_info(self):
        ...
```

```python
class Admin(User):

    def display_info(self):
        ...
```

This is called **Method Overriding**.

The method has the same name, but each child class provides role-specific behavior.

---

## 🔁 Using `super()`

Each overridden method uses:

```python
super().display_info()
```

This allows the child class to reuse the common implementation from the parent class and then add its own role-specific information.

For example:

```python
def display_info(self):
    super().display_info()
    print("Role: Student")
    print(f"Course: {self.course}")
```

---

## 🔀 Polymorphism

The project also demonstrates polymorphism.

Different types of objects can be stored together:

```python
users = [
    student1,
    student2,
    mentor1,
    admin1
]
```

The same method can then be called:

```python
for user in users:
    user.display_info()
```

Python executes the appropriate overridden `display_info()` method based on the object.

```text
Student object → Student.display_info()
Mentor object  → Mentor.display_info()
Admin object   → Admin.display_info()
```

---

## 🧩 OOP Concepts Covered

| Concept | Demonstrated In |
|---|---|
| Class | `User`, `Student`, `Mentor`, `Admin` |
| Objects | `student1`, `student2`, `mentor1`, `admin1` |
| Constructor | `__init__()` |
| Instance Variables | `name`, `email`, `course`, `expertise` |
| Instance Methods | `submit_assignment()`, `assign_student()` |
| Inheritance | Child classes inherit from `User` |
| Hierarchical Inheritance | `User → Student, Mentor, Admin` |
| Method Overriding | `display_info()` |
| `super()` | Parent method reuse |
| Class Variable | `total_users` |
| Class Method | `get_total_users()` |
| Static Method | `validate_email()` |
| Polymorphism | Same method call with different objects |

---

## 📁 Project Structure

```text
mini-learning-platform/
│
├── user.py
├── student.py
├── mentor.py
├── admin.py
├── main.py
└── README.md
```

### `user.py`

Contains the parent `User` class.

### `student.py`

Contains the `Student` child class.

### `mentor.py`

Contains the `Mentor` child class.

### `admin.py`

Contains the `Admin` child class.

### `main.py`

Creates objects and demonstrates the complete application.

---

## ▶️ How to Run

### Step 1 — Open CMD

Navigate to the project directory:

```cmd
cd mini-learning-platform
```

### Step 2 — Run the program

```cmd
python main.py
```

---

## 🖥️ Application Flow

```text
Start
  ↓
Create Student objects
  ↓
Create Mentor object
  ↓
Create Admin object
  ↓
Student submits assignments
  ↓
Mentor assigns students
  ↓
Admin manages platform
  ↓
Call display_info()
  ↓
Method Overriding
  ↓
Polymorphism
  ↓
Display total users
  ↓
End
```

---

## 📋 Example Output

```text
========== STUDENT ACTIVITIES ==========
Rahul submitted: OOP Assignment
Rahul submitted: Inheritance Assignment
Priya submitted: Functions Assignment

========== MENTOR ACTIVITIES ==========
Rahul assigned to mentor Arun
Priya assigned to mentor Arun

========== ADMIN ACTIVITIES ==========
Admin Meena performed: Added a new Python course

========== METHOD OVERRIDING ==========

Student Information:
Name: Rahul
Role: Student
Course: Advanced Python

Mentor Information:
Name: Arun
Role: Mentor
Expertise: Python & AI

Admin Information:
Name: Meena
Role: Admin
Department: Learning Operations

========== CLASS METHOD ==========
Total Users: 4
```

---

## 🎥 YouTube Video Requirements

The video should explain the following:

### 1. Introduction

Explain the Learning Platform problem and what we are going to build.

### 2. Inheritance

Explain how `Student`, `Mentor`, and `Admin` inherit common functionality from `User`.

### 3. Class Relationship

Explain:

```text
User
├── Student
├── Mentor
└── Admin
```

### 4. Method Overriding

Explain why each child class has its own `display_info()` method.

### 5. `super()`

Explain how the child class reuses the parent implementation.

### 6. Polymorphism

Demonstrate:

```python
for user in users:
    user.display_info()
```

### 7. Code Walkthrough

Explain each Python file and the important methods.

### 8. Program Execution

Run:

```cmd
python main.py
```

and explain the output.

---

## 📦 GitHub Submission

Create a **public GitHub repository** and push the complete project.

Suggested repository name:

```text
mini-learning-platform-inheritance
```

The repository should contain:

```text
user.py
student.py
mentor.py
admin.py
main.py
README.md
```

Then submit the public repository URL as required by the assignment.

---

## 🚀 Possible Enhancements

After completing the basic assignment, you can extend the application with:

- Course registration
- Assignment scores
- Student progress percentage
- Mentor capacity
- Admin user management
- Course creation
- Course deletion
- Search by User ID
- Menu-driven CLI
- File/database storage

---

## 🎓 Learning Outcome

After completing this project, you should be able to explain:

```text
Inheritance
     ↓
Hierarchical Inheritance
     ↓
Method Overriding
     ↓
super()
     ↓
Polymorphism
```

The main takeaway is:

> **Inheritance allows child classes to reuse common functionality, while method overriding allows each child class to provide its own specialized behavior.**
