from employee import Developer


# Create Developer objects
developer1 = Developer(
    "EMP001",
    "Rahul",
    1200000,
    "Engineering",
    "Python",
    5
)

developer2 = Developer(
    "EMP002",
    "Priya",
    1400000,
    "Engineering",
    "Java",
    7
)

developer3 = Developer(
    "EMP003",
    "Arjun",
    1000000,
    "Product Engineering",
    "JavaScript",
    3
)


# Display details of Developer 1
print("\n========== Developer 1 ==========")
developer1.display_developer_details()


# Display details of Developer 2
print("\n========== Developer 2 ==========")
developer2.display_developer_details()


# Display details of Developer 3
print("\n========== Developer 3 ==========")
developer3.display_developer_details()


# Demonstrate inherited functionality
print("\n========== Inherited Method Demonstration ==========")

developer1.display_details()
developer2.display_details()
developer3.display_details()