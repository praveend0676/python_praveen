class Employee:
    """Represents an employee in an organization."""

    def __init__(
        self,
        employee_id,
        name,
        department,
        salary,
        designation
    ):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary
        self.designation = designation

    def display_info(self):
        """Display employee information."""

        print(f"Employee ID : {self.employee_id}")
        print(f"Name        : {self.name}")
        print(f"Department  : {self.department}")
        print(f"Salary      : ₹{self.salary:,.2f}")
        print(f"Designation : {self.designation}")

    def update_salary(self, new_salary):
        """Update employee salary."""

        self.salary = new_salary

        print(
            f"Salary updated successfully for "
            f"{self.name}"
        )

    def calculate_annual_salary(self):
        """Calculate and return annual salary."""

        return self.salary * 12