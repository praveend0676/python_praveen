# E-Commerce Product Management System Using Python OOP

## Problem Statement

Create a simple **Product Management System for an e-commerce application using Python Object-Oriented Programming (OOP)**.

The application should represent products available in an online store. Each product should maintain information such as its product ID, name, price, category, and available stock.

The application should allow users to view product details, update stock quantities, and calculate the total price when purchasing a specific quantity of a product.

In addition to instance methods, this exercise should demonstrate the use of a **static method** for validating product prices.

---

## 1. Create the `Product` Class

Create a class named:

```python
class Product:
```

Each product should contain the following attributes:

* `product_id` – Unique product identifier
* `name` – Product name
* `price` – Price of one unit
* `category` – Product category
* `stock_quantity` – Number of units currently available

For example:

```text
Product ID     : P001
Name           : Wireless Mouse
Price          : ₹799
Category       : Electronics
Stock Quantity : 25
```

---

## 2. Implement `display_product()`

Create an instance method:

```python
display_product()
```

This method should display all the information about a product.

Example:

```text
------ Product Details ------
Product ID     : P001
Name           : Wireless Mouse
Price          : ₹799.00
Category       : Electronics
Stock Quantity : 25
```

---

## 3. Implement `update_stock()`

Create an instance method:

```python
update_stock()
```

This method should update the available stock quantity.

For example, if the product currently has:

```text
Stock Quantity : 25
```

and 5 units are purchased:

```text
Purchased      : 5
Remaining Stock: 20
```

The method should update the product's stock accordingly.

The application should prevent the stock quantity from becoming negative.

---

## 4. Implement `calculate_total_price(quantity)`

Create an instance method:

```python
calculate_total_price(quantity)
```

This method should calculate the total price for purchasing a specified quantity.

For example:

```text
Product Price : ₹799
Quantity      : 3
```

The total price should be:

```text
₹799 × 3 = ₹2,397
```

The method should return the calculated total amount.

---

# 5. Create a Static Method

Create the following static method:

```python
@staticmethod
def is_valid_price(price):
```

The method should validate whether a product price is valid.

### Rule

* If the price is greater than `0`, return `True`.
* If the price is `0` or negative, return `False`.

Example:

```python
Product.is_valid_price(799)
```

Output:

```text
True
```

And:

```python
Product.is_valid_price(0)
```

Output:

```text
False
```

Similarly:

```python
Product.is_valid_price(-100)
```

should return:

```text
False
```

---

# 6. Why Use a Static Method?

The price validation does not depend on any particular product object.

For example:

```python
Product.is_valid_price(799)
```

We don't need:

```python
product1.is_valid_price(799)
```

because checking whether a number is greater than zero does not require access to:

* `self.name`
* `self.price`
* `self.stock_quantity`

Therefore, a **static method** is appropriate.

This exercise should help demonstrate the difference between:

```text
Instance Method → works with object data
Class Method    → works with class-level data
Static Method   → independent utility related to the class
```

---

# 7. Create at Least Five Products

Create at least **five different Product objects**.

For example:

```text
Product 1
ID       : P001
Name     : Wireless Mouse
Price    : ₹799
Category : Electronics
Stock    : 25

Product 2
ID       : P002
Name     : Mechanical Keyboard
Price    : ₹2,499
Category : Electronics
Stock    : 15

Product 3
ID       : P003
Name     : USB-C Cable
Price    : ₹499
Category : Accessories
Stock    : 40

Product 4
ID       : P004
Name     : Laptop Backpack
Price    : ₹1,299
Category : Bags
Stock    : 20

Product 5
ID       : P005
Name     : Water Bottle
Price    : ₹699
Category : Lifestyle
Stock    : 30
```

---

# 8. Demonstrate Purchasing a Product

Select one of the products and simulate a purchase.

For example:

```text
Product      : Wireless Mouse
Price        : ₹799
Available    : 25
Quantity     : 3
```

Calculate the total:

```text
Total Price: ₹2,397
```

Then update the stock:

```text
Previous Stock : 25
Purchased      : 3
Remaining Stock: 22
```

---

# 9. Demonstrate Stock Validation

The application should prevent a customer from purchasing more units than are available.

For example:

```text
Available Stock : 5
Requested       : 8
```

The purchase should be rejected:

```text
Insufficient stock.
Purchase cannot be completed.
```

The stock should remain unchanged.

---

# 10. Demonstrate Price Validation

Use the static method to validate different prices:

```python
print(Product.is_valid_price(999))
print(Product.is_valid_price(0))
print(Product.is_valid_price(-500))
```

Expected result:

```text
True
False
False
```

---

# Expected OOP Concepts

| OOP Concept        | Where It Is Used                 |
| ------------------ | -------------------------------- |
| Class              | `Product`                        |
| Objects            | `product1` to `product5`         |
| `__init__()`       | Initialize product information   |
| Instance Variables | ID, name, price, category, stock |
| Instance Methods   | `display_product()`              |
| Instance Methods   | `update_stock()`                 |
| Instance Methods   | `calculate_total_price()`        |
| Static Method      | `is_valid_price()`               |
| `@staticmethod`    | Price validation                 |
| Validation         | Price and stock validation       |

---

# Key Concept – Static Method

The main learning objective of this exercise is to understand a **static method**.

A static method belongs logically to the class but does not need access to either:

```text
self → object
```

or:

```text
cls → class
```

For example:

```python
@staticmethod
def is_valid_price(price):
    return price > 0
```

It can be called directly using:

```python
Product.is_valid_price(999)
```

The method simply receives the `price` and performs the validation.

---

# Final Objective

Build a small **E-Commerce Product Management System** that:

1. Creates a `Product` class.
2. Creates at least five product objects.
3. Stores product ID, name, price, category, and stock quantity.
4. Displays product information.
5. Calculates the total price for a requested quantity.
6. Updates stock after a purchase.
7. Prevents purchases when stock is insufficient.
8. Uses a static method to validate product prices.
9. Demonstrates the difference between an instance method and a static method.

## Main Learning Goal

The key idea is:

> **Use instance methods when the operation needs information from a particular object, and use a static method when the operation is related to the class but does not need object or class data.**

This exercise builds naturally on the previous **Banking Application** and **Employee Inheritance** exercises and introduces the next important OOP concept: **`@staticmethod`**.
