# Student Management System

A simple **Student Management System built using Python and Object-Oriented Programming (OOP)**.

## 📌 Description

This project demonstrates how Python classes and objects can be used to manage student information.

The system allows us to:

* Create multiple student objects
* Store student details
* Display student information
* Update marks
* Calculate average marks
* Track the total number of students

## 🧠 Concepts Covered

* Class
* Objects
* `__init__()`
* Instance attributes
* Instance methods
* `self`
* Class variable
* Class method
* Basic Python OOP

## 📂 Project Structure

```text
student_management_system/
│
├── student.py
├── main.py
└── README.md
```

## ▶️ How to Run

Make sure Python is installed.

Run the application from the project directory:

```bash
python main.py
```

## 🏗️ Main Class

The project contains a `Student` class with the following attributes:

* `name`
* `email`
* `student_id`
* `course`
* `marks`

### Methods

```text
display_details()
update_marks()
calculate_average()
get_total_students()
```

## 👨‍🎓 Example

```python
student1 = Student(
    "Rahul",
    "rahul@gmail.com",
    "ST001",
    "Python",
    [85, 90, 78]
)

student1.display_details()
```

## 🎯 Learning Objective

The main objective of this project is to understand how **OOP concepts can be applied to a real-world problem** by modeling a student as a Python object.
