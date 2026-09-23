from employee import Employee


# =====================================================
# CREATE EMPLOYEE OBJECTS
# =====================================================

employee1 = Employee(
    "EMP101",
    "Rahul",
    "IT",
    60000,
    "Software Engineer"
)

employee2 = Employee(
    "EMP102",
    "Priya",
    "HR",
    55000,
    "HR Executive"
)

employee3 = Employee(
    "EMP103",
    "Arun",
    "Finance",
    70000,
    "Financial Analyst"
)

employee4 = Employee(
    "EMP104",
    "Sneha",
    "Marketing",
    65000,
    "Marketing Manager"
)

employee5 = Employee(
    "EMP105",
    "Vijay",
    "IT",
    80000,
    "Senior Software Engineer"
)


# =====================================================
# STORE EMPLOYEES IN A LIST
# =====================================================

employees = [
    employee1,
    employee2,
    employee3,
    employee4,
    employee5
]


# =====================================================
# DISPLAY EMPLOYEE INFORMATION
# =====================================================

print("=" * 60)
print("          EMPLOYEE MANAGEMENT SYSTEM")
print("=" * 60)

print("\nEMPLOYEE DETAILS")
print("-" * 60)

for employee in employees:

    employee.display_info()

    annual_salary = employee.calculate_annual_salary()

    print(
        f"Annual Salary: ₹{annual_salary:,.2f}"
    )

    print("-" * 60)


# =====================================================
# UPDATE SALARY
# =====================================================

print("\nUPDATING SALARY")
print("-" * 60)

employee1.update_salary(70000)

print()


# =====================================================
# DISPLAY UPDATED INFORMATION
# =====================================================

print("UPDATED EMPLOYEE DETAILS")
print("-" * 60)

employee1.display_info()

print(
    f"Annual Salary: "
    f"₹{employee1.calculate_annual_salary():,.2f}"
)

print("-" * 60)


# =====================================================
# ANNUAL SALARY REPORT
# =====================================================

print("\nANNUAL SALARY REPORT")
print("-" * 60)

for employee in employees:

    annual_salary = (
        employee.calculate_annual_salary()
    )

    print(
        f"{employee.name:<15} "
        f"₹{annual_salary:,.2f}"
    )