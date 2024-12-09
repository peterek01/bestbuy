
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if not name:
            raise ValueError("Name cannot be empty.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if quantity < 0:
            raise ValueError("Quantity must be greater than zero.")

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        if self.quantity > 0:
            self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.get_quantity()}"

    def buy(self, quantity) -> float:
        if not self.active:
            raise Exception("The product is inactive and cannot be purchased.")
        if quantity > self.quantity:
            raise Exception("Insufficient product in stock.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return quantity * self.price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def buy(self, amount):
        if not self.is_active():
            raise ValueError(f"The product '{self.name}' is not active.")
        return amount * self.price

    def show(self):
        return f"{self.name} (Non-stocked), Prise: {self.price}"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, max_per_order):
        super().__init__(name, price, quantity)
        self.max_per_order = max_per_order

    def buy(self, amount):
        if amount > self.max_per_order:
            raise ValueError(f"Cannot buy {amount}. Maximum allowed per order is {self.max_per_order}.")
        return super().buy(amount)

    def show(self):
        return (
            f"{self.name} (Limited), Price: {self.price}, "
            f"Quantity: {self.quantity}, Max per order: {self.max_per_order}"
        )
