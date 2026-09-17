class Product:
    """
    Represents a product in an e-commerce application.
    """

    def __init__(self, product_id, name, price, category, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity

    def display_product(self):
        """Display product details."""
        print("\n------ Product Details ------")
        print(f"Product ID     : {self.product_id}")
        print(f"Name           : {self.name}")
        print(f"Price          : Rs.{self.price:,.2f}")
        print(f"Category       : {self.category}")
        print(f"Stock Quantity : {self.stock_quantity}")

    def update_stock(self, quantity):
        """
        Reduce stock when a product is purchased.
        """

        if quantity <= 0:
            print("Purchase quantity must be greater than zero.")
            return

        if quantity > self.stock_quantity:
            print(
                f"Insufficient stock for {self.name}. "
                f"Available stock: {self.stock_quantity}"
            )
            return

        self.stock_quantity -= quantity

        print(f"{quantity} unit(s) purchased successfully.")
        print(f"Remaining stock: {self.stock_quantity}")

    def calculate_total_price(self, quantity):
        """
        Calculate the total price for the requested quantity.
        """

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return 0

        if quantity > self.stock_quantity:
            print(
                f"Insufficient stock. "
                f"Available stock: {self.stock_quantity}"
            )
            return 0

        return self.price * quantity

    @staticmethod
    def is_valid_price(price):
        """
        Validate product price.

        Returns True if price is greater than zero.
        Otherwise, returns False.
        """

        return price > 0
