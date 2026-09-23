# 💳 Payment Processing System Using Python OOP

## 📌 Project Overview

This project demonstrates **Abstraction, Inheritance, Method Overriding, and Runtime Polymorphism** using a simple payment-processing application built with Python Object-Oriented Programming.

The application supports three different payment methods:

* 💳 Credit Card
* 📱 UPI
* 🏦 Net Banking

Although each payment method works differently, all payment types follow a common contract defined by an abstract `Payment` class.

---

## 🎯 Problem Statement

Build a payment-processing example with an abstract `Payment` class containing a `pay()` method.

Implement the following payment classes:

```text
                    Payment
                 << Abstract >>
                       |
          ______________|_______________
         |              |               |
         ↓              ↓               ↓
CreditCardPayment   UPIPayment   NetBankingPayment
```

Each child class should implement its own version of the `pay()` method.

The application should demonstrate **runtime polymorphism** by calling the same method on different payment objects.

---

# 🧩 Key Requirements

The project should demonstrate:

* Abstract Class
* Abstract Method
* Inheritance
* Method Overriding
* Runtime Polymorphism
* Constructors
* Instance Variables
* Instance Methods
* `super()`
* Multiple Objects

---

# 📚 OOP Concepts

## 1. Abstraction

**Abstraction** means exposing the essential functionality while hiding implementation details.

In this project, `Payment` is an abstract class.

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass
```

The `Payment` class defines the common operation:

```text
pay()
```

but does not define how the payment should actually be processed.

The child classes provide the implementation.

---

# 2. Abstract Class

The `Payment` class inherits from Python's `ABC` class.

```python
class Payment(ABC):
```

`ABC` stands for **Abstract Base Class**.

An abstract class is intended to serve as a common blueprint for its child classes.

---

# 3. Abstract Method

The `pay()` method is marked using:

```python
@abstractmethod
```

Example:

```python
@abstractmethod
def pay(self):
    pass
```

This means that concrete child classes must implement `pay()`.

---

# 4. Inheritance

The payment classes inherit from the abstract `Payment` class.

```text
Payment
   |
   +---- CreditCardPayment
   |
   +---- UPIPayment
   |
   +---- NetBankingPayment
```

For example:

```python
class CreditCardPayment(Payment):
    ...
```

This allows the child class to reuse functionality from the parent class.

---

# 5. Method Overriding

Each child class implements its own version of:

```python
pay()
```

### Credit Card

```python
def pay(self):
    print("Processing Credit Card payment")
```

### UPI

```python
def pay(self):
    print("Processing UPI payment")
```

### Net Banking

```python
def pay(self):
    print("Processing Net Banking payment")
```

The method name is the same, but the implementation is different.

This is called **Method Overriding**.

---

# 6. Runtime Polymorphism ⭐

Runtime polymorphism is the main concept demonstrated by this project.

Create different payment objects:

```python
credit_card = CreditCardPayment(...)
upi = UPIPayment(...)
net_banking = NetBankingPayment(...)
```

Store them together:

```python
payments = [
    credit_card,
    upi,
    net_banking
]
```

Then call the same method:

```python
for payment in payments:
    payment.pay()
```

Although the method call is the same:

```python
payment.pay()
```

Python determines at runtime which implementation should be executed.

```text
CreditCardPayment object
        ↓
payment.pay()
        ↓
CreditCardPayment.pay()


UPIPayment object
        ↓
payment.pay()
        ↓
UPIPayment.pay()


NetBankingPayment object
        ↓
payment.pay()
        ↓
NetBankingPayment.pay()
```

This is **Runtime Polymorphism**.

---

# 🔗 Relationship Between the Concepts

The concepts in this project are connected:

```text
                ABSTRACTION
                     ↓
             Abstract Payment
                     ↓
                INHERITANCE
                     ↓
       ┌─────────────┼─────────────┐
       ↓             ↓             ↓
 Credit Card        UPI       Net Banking
       │             │             │
       └─────────────┼─────────────┘
                     ↓
             METHOD OVERRIDING
                     ↓
              Different pay()
                     ↓
          RUNTIME POLYMORPHISM
                     ↓
              payment.pay()
```

### Simple explanation

> **Abstraction defines what a payment must do.**

> **Inheritance allows different payment classes to follow the common structure.**

> **Method overriding allows each payment class to define its own implementation.**

> **Runtime polymorphism allows the appropriate implementation to be selected at runtime.**


---
# 📊 OOP Concepts Summary

| Concept              | Example                         |
| -------------------- | ------------------------------- |
| Abstract Class       | `Payment`                       |
| Abstract Method      | `pay()`                         |
| Inheritance          | Payment → child classes         |
| Method Overriding    | Each child implements `pay()`   |
| Constructor          | `__init__()`                    |
| Instance Variable    | `amount`, `upi_id`, `bank_name` |
| `super()`            | Child constructors              |
| Runtime Polymorphism | `payment.pay()`                 |
| Multiple Objects     | Three payment objects           |

---

# 📌 Key Takeaway

```text
Payment
   │
   │  abstract pay()
   │
   ├───────────────┬─────────────────┐
   ↓               ↓                 ↓
Credit Card       UPI           Net Banking
   │               │                 │
   pay()           pay()             pay()
   │               │                 │
   └───────────────┴─────────────────┘
                   ↓
          Runtime Polymorphism
```

### ⭐ Remember

> **Abstraction tells us WHAT a class should do.**

> **Implementation tells us HOW it should do it.**

> **Runtime polymorphism allows the appropriate implementation to be selected based on the actual object at runtime.**

---


# 🎓 Learning Outcomes

After completing this project, you should be able to:

* Create an abstract class in Python
* Use `ABC`
* Use `@abstractmethod`
* Understand inheritance
* Implement abstract methods
* Override methods in child classes
* Understand runtime polymorphism
* Use `super()`
* Work with multiple objects
* Explain the difference between abstraction and polymorphism
* Build a small real-world OOP application

---

## 🔑 Final Concept

```text
Abstract Class
      ↓
Common Contract
      ↓
Child Classes
      ↓
Method Overriding
      ↓
Same Method Call
      ↓
Different Runtime Behavior
      ↓
Runtime Polymorphism
```
