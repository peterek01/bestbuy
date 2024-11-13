class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name cannot be empty.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = quantity > 0

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity: float):
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.get_quantity()}"

    def buy(self, quantity: float) -> float:
        if not self.active:
            raise Exception("The product is inactive and cannot be purchased.")
        if quantity > self.quantity:
            raise Exception("Insufficient product in stock.")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price


try:
    product = Product("Laptop", 10, 5)
    print(product.show())
except ValueError as e:
    print(e)


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("BacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()