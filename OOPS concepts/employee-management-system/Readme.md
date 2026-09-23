# 👨‍💼 Employee Management System Using Python OOP

## 📌 Problem Statement

Create a simple **Employee Management System** using Python Object-Oriented Programming (OOP).

The application should maintain employee information and provide basic operations such as:

* Displaying employee information
* Updating employee salary
* Calculating annual salary

The objective of this project is to understand how **classes, objects, constructors, instance variables, and instance methods** can be used to build a simple real-world application.

---

# 🎯 What to Build

Create an `Employee` class with the following properties:

```text
Employee
│
├── Employee ID
├── Name
├── Department
├── Salary
└── Designation
```

The `Employee` class should provide the following methods:

```text
Employee
│
├── display_info()
├── update_salary()
└── calculate_annual_salary()
```

---

# 🧩 Employee Class

Create a class called:

```python
class Employee:
```

The class should contain the following attributes.

### 1. Employee ID

A unique identifier for the employee.

Example:

```text
EMP101
```

### 2. Name

The employee's name.

Example:

```text
Rahul
```

### 3. Department

The department in which the employee works.

Example:

```text
IT
```

### 4. Salary

The employee's monthly salary.

Example:

```text
60000
```

### 5. Designation

The employee's job designation.

Example:

```text
Software Engineer
```

---

# 🔧 Required Methods

## 1. `display_info()`

Create a method:

```python
def display_info(self):
```

This method should display all information about the employee.

Example:

```text
Employee ID : EMP101
Name        : Rahul
Department  : IT
Salary      : ₹60,000
Designation : Software Engineer
```

---

## 2. `update_salary()`

Create a method:

```python
def update_salary(self, new_salary):
```

This method should update the employee's existing salary.

Example:

```text
Old Salary : ₹60,000
New Salary : ₹70,000
```

After updating the salary, the employee object should contain the new salary.

---

## 3. `calculate_annual_salary()`

Create a method:

```python
def calculate_annual_salary(self):
```

The method should calculate the employee's annual salary using:

```text
Annual Salary = Monthly Salary × 12
```

Example:

```text
Monthly Salary : ₹60,000

Annual Salary:
₹60,000 × 12
= ₹7,20,000
```

The method should return the calculated annual salary.

---

# 👥 Employee Objects

Create **at least 5 employee objects**.

For example:

```python
employee1 = Employee(...)
employee2 = Employee(...)
employee3 = Employee(...)
employee4 = Employee(...)
employee5 = Employee(...)
```

Each employee should have different information.

Example:

| Employee ID | Name  | Department |  Salary | Designation              |
| ----------- | ----- | ---------- | ------: | ------------------------ |
| EMP101      | Rahul | IT         | ₹60,000 | Software Engineer        |
| EMP102      | Priya | HR         | ₹55,000 | HR Executive             |
| EMP103      | Arun  | Finance    | ₹70,000 | Financial Analyst        |
| EMP104      | Sneha | Marketing  | ₹65,000 | Marketing Manager        |
| EMP105      | Vijay | IT         | ₹80,000 | Senior Software Engineer |

---

# 📚 OOP Concepts to Demonstrate

This assignment should demonstrate the following Python OOP concepts.

## 1. Class

```python
class Employee:
```

The `Employee` class acts as a blueprint for employee objects.

---

## 2. Objects

Create at least five objects:

```python
employee1 = Employee(...)
employee2 = Employee(...)
employee3 = Employee(...)
employee4 = Employee(...)
employee5 = Employee(...)
```

Each object represents an individual employee.

---

## 3. Constructor

Use the `__init__()` constructor to initialize employee information.

```python
def __init__(
    self,
    employee_id,
    name,
    department,
    salary,
    designation
):
```

---

## 4. Instance Variables

The employee object should contain:

```python
self.employee_id
self.name
self.department
self.salary
self.designation
```

Each employee object maintains its own values.

---

## 5. Instance Methods

Implement:

```python
display_info()
update_salary()
calculate_annual_salary()
```

These methods operate on individual employee objects.

---

# 🔄 Suggested Program Flow

```text
Start
  ↓
Create Employee class
  ↓
Define employee attributes
  ↓
Create constructor
  ↓
Create display_info()
  ↓
Create update_salary()
  ↓
Create calculate_annual_salary()
  ↓
Create 5 Employee objects
  ↓
Store employees in a list
  ↓
Display employee information
  ↓
Calculate annual salary
  ↓
Update salary
  ↓
Display updated information
  ↓
Generate annual salary report
  ↓
End
```

---

# 🖥️ Expected Functionality

The application should be able to:

### Display employees

```text
========== EMPLOYEE DETAILS ==========

Employee ID : EMP101
Name        : Rahul
Department  : IT
Salary      : ₹60,000
Designation : Software Engineer
Annual Salary: ₹7,20,000
```

### Update salary

```text
========== UPDATE SALARY ==========

Employee: Rahul
Old Salary: ₹60,000
New Salary: ₹70,000

Salary updated successfully.
```

### Calculate annual salary

```text
========== ANNUAL SALARY ==========

Rahul : ₹8,40,000
Priya : ₹6,60,000
Arun  : ₹8,40,000
...
```

---

# 📁 Suggested Project Structure

```text
employee-management-system/
│
├── employee.py
├── main.py
└── README.md
```

### `employee.py`

Contains the `Employee` class and its methods.

### `main.py`

Creates employee objects and demonstrates the functionality.

### `README.md`

Contains the project problem statement, implementation details, execution instructions, and learning outcomes.

---

# ▶️ How to Run

## Step 1 — Open Command Prompt

Navigate to the project directory:

```cmd
cd employee-management-system
```

## Step 2 — Run the program

```cmd
python main.py
```

---

# 🎥 YouTube Video Requirement

Record a YouTube video explaining the complete implementation.

The video should cover:

### 1. Introduction

Explain what the Employee Management System does.

### 2. Problem Statement

Explain the employee attributes:

```text
Employee ID
Name
Department
Salary
Designation
```

### 3. Class

Explain:

```python
class Employee:
```

### 4. Constructor

Explain:

```python
def __init__(...):
```

and how the employee information is initialized.

### 5. Methods

Explain:

```text
display_info()
update_salary()
calculate_annual_salary()
```

### 6. Objects

Demonstrate the creation of at least five employee objects.

### 7. Program Execution

Run:

```cmd
python main.py
```

### 8. Output

Explain the displayed employee information, updated salary, and annual salary.

---

# 🎓 Learning Outcomes

After completing this project, you should understand:

* How to create a Python class
* How to create objects
* How constructors work
* How instance variables store object data
* How instance methods work
* How multiple objects can be created from one class
* How to store objects in a list
* How to update object data
* How to calculate values using object data
* How OOP can model a real-world entity


# ⭐ Final Learning Message

> **A class is a blueprint, and objects are real instances created from that blueprint.**

In this project:

```text
              Employee Class
                    │
       ┌────────────┼────────────┐
       ↓            ↓            ↓
   Employee 1   Employee 2   Employee 3
       ↓            ↓            ↓
   Employee 4   Employee 5
```

All employees are created from the same `Employee` class, but each object maintains its own employee information.

This demonstrates the fundamental OOP concepts of **Class, Object, Constructor, Instance Variables, and Instance Methods**.
