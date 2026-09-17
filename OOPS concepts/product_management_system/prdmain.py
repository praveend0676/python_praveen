from product import Product


# --------------------------------------------------
# Create Product Objects
# --------------------------------------------------

product1 = Product(
    "P001",
    "Wireless Mouse",
    799,
    "Electronics",
    25
)

product2 = Product(
    "P002",
    "Mechanical Keyboard",
    2499,
    "Electronics",
    15
)

product3 = Product(
    "P003",
    "USB-C Cable",
    499,
    "Accessories",
    40
)

product4 = Product(
    "P004",
    "Laptop Backpack",
    1299,
    "Bags",
    20
)

product5 = Product(
    "P005",
    "Water Bottle",
    699,
    "Lifestyle",
    30
)


# --------------------------------------------------
# Display Product Details
# --------------------------------------------------

print("\n========== ALL PRODUCTS ==========")

product1.display_product()
product2.display_product()
product3.display_product()
product4.display_product()
product5.display_product()


# --------------------------------------------------
# Calculate Total Price
# --------------------------------------------------

print("\n========== PURCHASE CALCULATION ==========")

quantity = 3

total_price = product1.calculate_total_price(quantity)

if total_price > 0:
    print(f"Product  : {product1.name}")
    print(f"Price    : Rs.{product1.price:,.2f}")
    print(f"Quantity : {quantity}")
    print(f"Total    : Rs.{total_price:,.2f}")


# --------------------------------------------------
# Update Stock After Purchase
# --------------------------------------------------

print("\n========== STOCK UPDATE ==========")

product1.update_stock(3)


# --------------------------------------------------
# Display Updated Product
# --------------------------------------------------

print("\n========== UPDATED PRODUCT ==========")

product1.display_product()


# --------------------------------------------------
# Demonstrate Insufficient Stock
# --------------------------------------------------

print("\n========== STOCK VALIDATION ==========")

product2.update_stock(20)


# --------------------------------------------------
# Demonstrate Static Method
# --------------------------------------------------

print("\n========== PRICE VALIDATION ==========")

print("Price Rs.999:", Product.is_valid_price(999))
print("Price Rs.0  :", Product.is_valid_price(0))
print("Price -Rs.500:", Product.is_valid_price(-500))
