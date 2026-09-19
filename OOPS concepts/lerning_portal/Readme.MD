🎓 Mini Super30 Learning Platform Using Python OOP

📌 Problem Statement

Build a mini Super30 Learning Platform using Python Object-Oriented
Programming (OOP).

The application should manage different types of users in a learning
platform, such as Students and Mentors.

Create a parent class called User that contains the common information
shared by all users.

The User class should contain:

Name

Email

User ID

Then create two child classes:

                    User
                   /    \
                  /      \
             Student     Mentor

The Student class should inherit from User and add:

Course Name

Completed Assignments

The Mentor class should inherit from User and add:

Expertise

Number of Students Assigned

The application should support functionality such as:

Registering students

Assigning a course to a student

Submitting an assignment

Displaying student information

Displaying mentor information

Counting the total number of users

🧩 OOP Requirements

Students must demonstrate the following Python OOP concepts:

Classes and Objects

Constructors

Instance Variables

Instance Methods

Inheritance

Hierarchical Inheritance

Multiple Objects

Class Variable

Class Method

Static Method

Code Reusability

Use of super()

🌳 Inheritance Structure

This assignment uses Hierarchical Inheritance.

                         User
                        /    \
                       /      \
                  Student     Mentor

There is one parent class, User, and multiple child classes, Student
and Mentor.

Parent Class

class User:
    pass

Child Classes

class Student(User):
    pass


class Mentor(User):
    pass

📋 Suggested Class Design

User

Common attributes:

name
email
user_id

Suggested functionality:

display_user_info()
get_total_users()
validate_email()

The class should also maintain a class variable such as:

total_users = 0

Student

Additional attributes:

course_name
completed_assignments

Suggested methods:

assign_course()
submit_assignment()
display_student_info()

Mentor

Additional attributes:

expertise
students_assigned

Suggested methods:

assign_student()
display_mentor_info()

⚙️ Required OOP Features

1. Class Variable

Use a class variable to maintain the total number of users.

Example:

total_users = 0

Every time a new user object is created, the count should increase.

2. Class Method

Create a class method to return the total number of users.

Example:

@classmethod
def get_total_users(cls):
    return cls.total_users

3. Static Method

Create a static method for functionality that does not depend on a
specific object or class state.

For example:

@staticmethod
def validate_email(email):
    return "@" in email and "." in email

4. Constructor

Use __init__() to initialize object data.

5. Inheritance

Student and Mentor should inherit common properties and methods from
User.

6. Multiple Objects

Create multiple student objects and at least one mentor object to
demonstrate object creation and reuse.

🖥️ Example Scenario

Create two students:

Student 1
Name: Rahul
Course: Python & AI

Student 2
Name: Priya
Course: Data Science

Create one mentor:

Mentor
Name: Arun
Expertise: Python & AI
Students Assigned: 2

Perform operations such as:

1. Display student information
2. Assign a course
3. Submit assignments
4. Display mentor information
5. Assign students to a mentor
6. Validate an email
7. Display total number of users

🎯 Learning Outcomes

After completing this assignment, students should be able to:

Create classes and objects in Python

Use constructors to initialize objects

Define and use instance methods

Understand inheritance

Explain hierarchical inheritance

Use class variables

Create class methods

Create static methods

Work with multiple objects

Reuse parent-class functionality

Use super()

Design a small real-world OOP application

⭐ Challenge

As an optional enhancement, add:

Course completion percentage

Mentor-student mapping

Assignment scores

Course fee

Student progress tracking

Search student by user ID

Remove or update a student

Menu-driven command-line interface

📌 Key Concept to Remember

One Parent Class
       +
Multiple Child Classes
       =
Hierarchical Inheritance

For this assignment:

                    User
                   /    \
                  /      \
             Student     Mentor

User → Student, Mentor = Hierarchical Inheritance