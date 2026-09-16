# Employee Management System Using Python OOP – Inheritance

## Problem Statement

Create a simple **Employee Management System using Python Object-Oriented Programming (OOP)** to demonstrate the concept of **Inheritance**.

In this exercise, we will create a **parent class** called `Employee` that contains common information and functionality applicable to all employees.

We will then create a **child class** called `Developer`, which inherits the properties and methods of the `Employee` class and adds developer-specific information.

The objective is to understand how a child class can **reuse functionality from a parent class** while also having its own additional attributes and behavior.

---

# 1. Create the Parent Class – `Employee`

Create a class named:

```python
Employee
```

The `Employee` class should contain the following attributes:

* `employee_id` – Unique employee ID
* `name` – Employee name
* `salary` – Employee salary
* `department` – Employee's department

Use the `__init__()` method to initialize these attributes.

### Example

```text
Employee ID : EMP001
Name        : Rahul
Salary      : ₹12,00,000
Department  : Engineering
```

---

# 2. Create `display_details()` Method

The `Employee` class should contain an instance method:

```python
display_details()
```

This method should display the common employee information.

### Example Output

```text
------ Employee Details ------
Employee ID : EMP001
Name        : Rahul
Salary      : ₹12,00,000
Department  : Engineering
```

---

# 3. Create the Child Class – `Developer`

Create another class called:

```python
Developer
```

The `Developer` class should **inherit from the `Employee` class**.

The relationship should be:

```text
             Employee
                │
                │ inherits
                ▼
             Developer
```

The `Developer` class should contain all the attributes of `Employee` and additional developer-specific information.

### Additional attributes

* `programming_language` – Programming language used by the developer
* `experience` – Years of development experience

For example:

```text
Programming Language : Python
Experience           : 5 years
```

---

# 4. Use Inheritance

The `Developer` class should inherit from `Employee`.

Example:

```python
class Developer(Employee):
    ...
```

The child class should be able to use the functionality defined in the parent class.

For example, if `display_details()` is defined in `Employee`, a `Developer` object should be able to call:

```python
developer1.display_details()
```

without defining the same method again in the child class.

This demonstrates **code reuse through inheritance**.

---

# 5. Create Developer Objects

Create at least **three Developer objects** with different information.

For example:

```text
Developer 1
Employee ID         : EMP001
Name                : Rahul
Salary              : ₹12,00,000
Department          : Engineering
Programming Language: Python
Experience          : 5 years


Developer 2
Employee ID         : EMP002
Name                : Priya
Salary              : ₹14,00,000
Department          : Engineering
Programming Language: Java
Experience          : 7 years


Developer 3
Employee ID         : EMP003
Name                : Arjun
Salary              : ₹10,00,000
Department          : Product Engineering
Programming Language: JavaScript
Experience          : 3 years
```

---

# 6. Demonstrate Parent Class Functionality

For each `Developer` object, demonstrate that it can access the method inherited from the `Employee` class.

For example:

```python
developer1.display_details()
developer2.display_details()
developer3.display_details()
```

The output should demonstrate that the `Developer` objects can use functionality defined in the `Employee` parent class.

---

# 7. Display Developer-Specific Information

The application should also display the additional information specific to a developer.

For example:

```text
------ Developer Details ------
Employee ID          : EMP001
Name                 : Rahul
Salary               : ₹12,00,000
Department           : Engineering
Programming Language : Python
Experience           : 5 years
```

You may create a separate method such as:

```python
display_developer_details()
```

to display the additional developer information.

---

# Expected Class Structure

The basic design should look like this:

```text
                    Employee
                       │
              ┌────────┴────────┐
              │                 │
        Common Attributes    display_details()
              │
              │
              ▼
          Developer
              │
       ┌──────┴───────┐
       │              │
Programming       Experience
 Language
```

---

# Expected OOP Concepts

This exercise should demonstrate the following concepts:

| OOP Concept        | Where It Is Used                         |
| ------------------ | ---------------------------------------- |
| Class              | `Employee`, `Developer`                  |
| Object             | `developer1`, `developer2`, `developer3` |
| Parent Class       | `Employee`                               |
| Child Class        | `Developer`                              |
| Inheritance        | `Developer(Employee)`                    |
| `__init__()`       | Initialize employee/developer data       |
| Instance Variables | Employee and developer information       |
| Instance Methods   | `display_details()`                      |
| Code Reuse         | Developer uses Employee functionality    |

---

# Key Concept – Inheritance

The main objective of this exercise is to understand **Inheritance**.

Inheritance allows a child class to acquire properties and methods from a parent class.

For example:

```python
class Employee:

    def display_details(self):
        print("Employee details")


class Developer(Employee):
    pass
```

Now:

```python
developer1 = Developer()

developer1.display_details()
```

The `Developer` object can use:

```python
display_details()
```

even though the method was defined inside the `Employee` class.

This is **inheritance and code reuse**.

---

# Real-World Relationship

The relationship can be explained using a simple real-world example:

```text
Employee
   │
   ├── Employee ID
   ├── Name
   ├── Salary
   └── Department
          │
          ▼
      Developer
          │
          ├── Programming Language
          └── Experience
```

A **Developer is an Employee**, but a Developer has additional information specific to the developer role.

This is an example of an **"is-a" relationship**:

> **Developer is an Employee.**

---

# Final Objective

Build a small Employee Management System where:

1. `Employee` acts as the **parent class**.
2. `Developer` acts as the **child class**.
3. `Developer` inherits common employee information and functionality.
4. Developer-specific information is added to the child class.
5. At least three Developer objects are created.
6. Each Developer object demonstrates access to the parent's `display_details()` method.

The primary goal is to understand how **Inheritance allows us to reuse existing functionality instead of duplicating code**.
