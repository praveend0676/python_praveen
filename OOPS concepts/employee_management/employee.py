class Employee:
    """
    Parent class representing a general employee.
    """

    def __init__(self, employee_id, name, salary, department):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.department = department

    def display_details(self):
        """Display common employee details."""
        print("\n------ Employee Details ------")
        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Salary      : ₹{self.salary:,.2f}")
        print(f"Department  : {self.department}")


class Developer(Employee):
    """
    Child class representing a Developer.
    Inherits from Employee.
    """

    def __init__(
        self,
        employee_id,
        name,
        salary,
        department,
        programming_language,
        experience
    ):
        # Call the parent class constructor
        super().__init__(
            employee_id,
            name,
            salary,
            department
        )

        # Developer-specific attributes
        self.programming_language = programming_language
        self.experience = experience

    def display_developer_details(self):
        """Display employee and developer-specific details."""

        # Reuse the method inherited from Employee
        self.display_details()

        print(f"Programming Language : {self.programming_language}")
        print(f"Experience           : {self.experience} years")
