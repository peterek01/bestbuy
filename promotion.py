from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        pass


class PercentageDiscountPromotion(Promotion):
    def __init__(self, how_much: str, discount_percentage: float):
        super().__init__("Percentage Discount")
        self.how_much = how_much
        self.discount_percentage = discount_percentage

    def apply_promotion(self, product, quantity):
        total_price = product.price * quantity
        discount = total_price * (self.discount_percentage / 100)
        final_price = total_price - discount
        return final_price, f"Applied {self.how_much} discount."


class SecondItemHalfPricePromotion(Promotion):
    def __init__(self):
        super().__init__("Second Item at Half Price")

    def apply_promotion(self, product, quantity):
        total_price = product.price * quantity
        if quantity > 1:
            # Discount on the second product (50%)
            discount = product.price / 2
            # For each pair of products, the second one is half the price
            total_price -= discount * (quantity // 2)
        return total_price, "Applied 'Second Item at Half Price' promotion."


class Buy2Get1FreePromotion(Promotion):
    def __init__(self):
        super().__init__("Buy 2, Get 1 Free")

    def apply_promotion(self, product, quantity):
        total_price = product.price * quantity
        if quantity >= 3:
            # Every third product is free
            discount = product.price * (quantity // 3)
            total_price -= discount
        return total_price, "Applied 'Buy 2, Get 1 Free' promotion."
