class Vehicle:
    def __init__(self, vehicle_number, brand, model, rental_price_per_day):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day

    def show_vehicle_details(self):
        print("\n------ Vehicle Details ------")
        print(f"Vehicle Number       : {self.vehicle_number}")
        print(f"Brand                : {self.brand}")
        print(f"Model                : {self.model}")
        print(f"Rental Price / Day   : ₹{self.rental_price_per_day:,.2f}")

    def calculate_rent(self, days):
        if not Vehicle.is_valid_rental_duration(days):
            print("Rental duration must be greater than zero.")
            return 0

        total_rent = self.rental_price_per_day * days

        print(f"Rental Days          : {days}")
        print(f"Total Rent           : ₹{total_rent:,.2f}")

        return total_rent

    @staticmethod
    def is_valid_rental_duration(days):
        return days > 0


class Car(Vehicle):
    def __init__(
        self,
        vehicle_number,
        brand,
        model,
        rental_price_per_day,
        number_of_seats
    ):
        super().__init__(
            vehicle_number,
            brand,
            model,
            rental_price_per_day
        )

        self.number_of_seats = number_of_seats

    def show_vehicle_details(self):
        super().show_vehicle_details()
        print(f"Number of Seats      : {self.number_of_seats}")


class Bike(Vehicle):
    def __init__(
        self,
        vehicle_number,
        brand,
        model,
        rental_price_per_day,
        engine_capacity
    ):
        super().__init__(
            vehicle_number,
            brand,
            model,
            rental_price_per_day
        )

        self.engine_capacity = engine_capacity

    def show_vehicle_details(self):
        super().show_vehicle_details()
        print(f"Engine Capacity      : {self.engine_capacity} CC")

