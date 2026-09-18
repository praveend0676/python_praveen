# 🚗 Mini Vehicle Rental Application Using Python OOP

## 📌 Problem Statement

Build a simple **Vehicle Rental Application** using Python Object-Oriented Programming (OOP).

The application should allow a rental company to manage different types of vehicles such as **Cars** and **Bikes**.

Create a parent class called `Vehicle` that contains the common information shared by all vehicles.

The `Vehicle` class should contain:

* Vehicle Number
* Brand
* Model
* Rental Price Per Day

Then create two child classes:

```text
                    Vehicle
                   /       \
                 Car       Bike
```

The `Car` class should inherit from `Vehicle` and add:

* Number of Seats

The `Bike` class should inherit from `Vehicle` and add:

* Engine Capacity

The application should calculate the total rental cost based on the number of rental days.

A static method should also be created to validate the rental duration. The rental duration must be greater than zero.

The application should create at least **2 cars and 2 bikes** and demonstrate the complete rental calculation and validation process.

---

# 🎯 Objectives

The main objective of this exercise is to understand how **Inheritance** can be used to model related objects in a real-world application.

The application should demonstrate:

1. Creating a parent class
2. Creating child classes
3. Reusing parent class functionality
4. Adding child-specific attributes
5. Using `super()`
6. Calculating rental cost
7. Validating input using a static method
8. Creating multiple objects

---

# 🏗️ Class Structure

```text
                         Vehicle
                            |
              +-------------+-------------+
              |                           |
             Car                         Bike
              |                           |
      Number of Seats              Engine Capacity
```

---

# 🚘 Vehicle Class

Create a parent class named:

```python
class Vehicle:
```

The class should contain the following attributes:

```text
vehicle_number
brand
model
rental_price_per_day
```

### Example

```text
Vehicle Number      : CAR001
Brand               : Toyota
Model               : Innova
Rental Price / Day  : ₹2,500
```

---

# 🚗 Car Class

Create a child class:

```python
class Car(Vehicle):
```

The `Car` class should inherit all common properties and methods from `Vehicle`.

It should additionally contain:

```text
number_of_seats
```

### Example

```text
Vehicle Number      : CAR001
Brand               : Toyota
Model               : Innova
Rental Price / Day  : ₹2,500
Number of Seats     : 7
```

---

# 🏍️ Bike Class

Create another child class:

```python
class Bike(Vehicle):
```

The `Bike` class should inherit all common properties and methods from `Vehicle`.

It should additionally contain:

```text
engine_capacity
```

### Example

```text
Vehicle Number      : BIKE001
Brand               : Royal Enfield
Model               : Classic 350
Rental Price / Day  : ₹1,200
Engine Capacity     : 350 CC
```

---

# 💰 Calculate Rental

Create the following method in the `Vehicle` class:

```python
calculate_rent(days)
```

The method should calculate the total rental cost.

### Formula

```text
Total Rent = Rental Price Per Day × Number of Days
```

### Example

```text
Rental Price Per Day = ₹2,500
Rental Duration      = 3 days

Total Rent = ₹2,500 × 3
           = ₹7,500
```

---

# 🛡️ Rental Duration Validation

Create a static method:

```python
@staticmethod
def is_valid_rental_duration(days):
```

The method should return:

```text
True
```

when the number of days is greater than zero.

It should return:

```text
False
```

when the number of days is zero or negative.

### Examples

```python
Vehicle.is_valid_rental_duration(5)
```

Output:

```text
True
```

```python
Vehicle.is_valid_rental_duration(0)
```

Output:

```text
False
```

```python
Vehicle.is_valid_rental_duration(-2)
```

Output:

```text
False
```

---

# 🔄 Use of `super()`

The child classes should use:

```python
super().__init__()
```

to call the parent `Vehicle` constructor.

This allows `Car` and `Bike` to reuse the common vehicle initialization logic.

For example:

```python
super().__init__(
    vehicle_number,
    brand,
    model,
    rental_price_per_day
)
```

---

# 🧪 Test Requirements

Create at least:

### 2 Cars

For example:

```text
Car 1:
Toyota Innova
7 Seats
₹2,500/day

Car 2:
Hyundai Creta
5 Seats
₹2,000/day
```

### 2 Bikes

For example:

```text
Bike 1:
Royal Enfield Classic 350
350 CC
₹1,200/day

Bike 2:
Yamaha MT-15
155 CC
₹900/day
```

---

# 📋 Required Operations

The application should demonstrate the following:

### 1. Display vehicle details

```python
car1.show_vehicle_details()
```

### 2. Calculate car rental

```python
car1.calculate_rent(3)
```

### 3. Calculate bike rental

```python
bike1.calculate_rent(2)
```

### 4. Test invalid duration

```python
car1.calculate_rent(0)
bike1.calculate_rent(-2)
```

### 5. Test the static method

```python
Vehicle.is_valid_rental_duration(5)
Vehicle.is_valid_rental_duration(0)
Vehicle.is_valid_rental_duration(-1)
```

---

# 📂 Project Structure

```text
vehicle_rental/
│
├── vehicle.py
├── main.py
└── README.md
```

### `vehicle.py`

Contains:

* `Vehicle`
* `Car`
* `Bike`

### `main.py`

Contains:

* Object creation
* Vehicle details
* Rental calculations
* Validation tests
* Static method demonstration

### `README.md`

Contains:

* Problem statement
* Requirements
* Class structure
* OOP concepts
* Execution instructions

---

# 🧠 OOP Concepts Covered

| OOP Concept        | Demonstration                     |
| ------------------ | --------------------------------- |
| Class              | `Vehicle`, `Car`, `Bike`          |
| Objects            | Car and Bike objects              |
| Constructor        | `__init__()`                      |
| Instance Variables | Vehicle-specific information      |
| Instance Methods   | `show_vehicle_details()`          |
| Inheritance        | `Car(Vehicle)`, `Bike(Vehicle)`   |
| `super()`          | Calling parent constructor/method |
| Method Reuse       | `calculate_rent()`                |
| Static Method      | `is_valid_rental_duration()`      |
| Validation         | Rental duration validation        |

---

# 🌍 Real-World Scenario

Consider a vehicle rental company.

The company rents different types of vehicles:

```text
Cars
 ├── Toyota Innova
 └── Hyundai Creta

Bikes
 ├── Royal Enfield Classic 350
 └── Yamaha MT-15
```

All vehicles have common information:

```text
Vehicle Number
Brand
Model
Rental Price
```

But different vehicle types have additional information.

### Car

```text
Number of Seats
```

### Bike

```text
Engine Capacity
```

Instead of creating completely separate classes with duplicated code, we can create a common `Vehicle` parent class and inherit from it.

This is one of the important practical uses of **Inheritance**.

---

# 🔑 Key Inheritance Concept

The relationship can be represented as:

```text
Car IS-A Vehicle

Bike IS-A Vehicle
```

Therefore, both `Car` and `Bike` can reuse functionality defined in `Vehicle`.

For example:

```python
car1.calculate_rent(3)
```

and:

```python
bike1.calculate_rent(2)
```

Both use the `calculate_rent()` functionality provided by the parent class.

---

# ⭐ Static Method Concept

The validation method:

```python
@staticmethod
def is_valid_rental_duration(days):
    return days > 0
```

does not need:

```text
self
```

or:

```text
cls
```

because it does not depend on a particular vehicle object or class-level data.

### Simple rule

```text
Instance Method → self → Object data

Class Method → cls → Class data

Static Method → neither → Independent utility logic
```

---

# ▶️ How to Run

Open the project folder in **VS Code**.

Open the terminal and run:

```bash
python main.py
```

---

# 📌 Expected Output

The application should display vehicle details and rental calculations similar to:

```text
------ Vehicle Details ------
Vehicle Number       : CAR001
Brand                : Toyota
Model                : Innova
Rental Price / Day   : ₹2,500.00
Number of Seats      : 7

Rental Days          : 3
Total Rent           : ₹7,500.00
```

For a bike:

```text
------ Vehicle Details ------
Vehicle Number       : BIKE001
Brand                : Royal Enfield
Model                : Classic 350
Rental Price / Day   : ₹1,200.00
Engine Capacity      : 350 CC

Rental Days          : 2
Total Rent           : ₹2,400.00
```

Invalid rental duration should display an appropriate validation message.

---

# 🚀 Possible Enhancements

Once the basic application is completed, you can extend it with:

* Vehicle availability status
* Customer details
* Booking functionality
* Rental start and end dates
* Late return charges
* Insurance charges
* Different pricing for weekends
* Discount calculation
* Customer registration
* Rental history
* Payment processing
* Vehicle maintenance tracking

---

# 🎓 Learning Outcome

After completing this exercise, you should be able to:

* Create parent and child classes
* Implement inheritance
* Reuse parent class functionality
* Add specialized child-class attributes
* Use `super()`
* Create and use instance methods
* Create and use static methods
* Perform input validation
* Model a real-world rental system using Python OOP

## 🏁 Key Takeaway

> **Inheritance allows us to create specialized classes such as Car and Bike from a common Vehicle class, while reusing shared properties and functionality.**

| Type         | Structure                        | Your example? |
| ------------ | -------------------------------- | ------------- |
| Single       | `A → B`                          |              |
| Multilevel   | `A → B → C`                      |              |
| Multiple     | `A + B → C`                      |             |
| Hierarchical | `A → B`, `A → C`                 |              |
| Hybrid       | Combination of inheritance types |             |
