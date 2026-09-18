from vehicle import Vehicle, Car, Bike


# Create Cars
car1 = Car(
    "CAR001",
    "Toyota",
    "Innova",
    2500,
    7
)

car2 = Car(
    "CAR002",
    "Hyundai",
    "Creta",
    2000,
    5
)


# Create Bikes
bike1 = Bike(
    "BIKE001",
    "Royal Enfield",
    "Classic 350",
    1200,
    350
)

bike2 = Bike(
    "BIKE002",
    "Yamaha",
    "MT-15",
    900,
    155
)


# Display Car Details
car1.show_vehicle_details()
car1.calculate_rent(3)

car2.show_vehicle_details()
car2.calculate_rent(5)


# Display Bike Details
bike1.show_vehicle_details()
bike1.calculate_rent(2)

bike2.show_vehicle_details()
bike2.calculate_rent(4)


# Test Invalid Rental Duration
print("\n------ Validation Test ------")

car1.calculate_rent(0)
bike1.calculate_rent(-2)


# Test Static Method Directly
print("\n------ Rental Duration Validation ------")

print(Vehicle.is_valid_rental_duration(5))
print(Vehicle.is_valid_rental_duration(0))
print(Vehicle.is_valid_rental_duration(-1))
