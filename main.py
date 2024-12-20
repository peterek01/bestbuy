from products import Product, NonStockedProduct, LimitedProduct
from promotion import PercentageDiscountPromotion, SecondItemHalfPricePromotion, Buy2Get1FreePromotion
from store import Store


def start(store: Store):
    while True:
        print("\nWelcome to the store! Please choose an option:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nAvailable products:")
            for idx, product in enumerate(store.get_all_products(), start=1):
                print(f"{idx}. {product}")
        elif choice == "2":
            print(f"\nTotal quantity in store: {store.get_total_quantity()}")
        elif choice == "3":
            print("\nMake an order:")
            shopping_list = []
            active_products = store.get_all_products()

            if not active_products:
                print("No products available for purchase.")
                continue

            print("Available products:")
            for idx, product in enumerate(active_products, start=1):
                print(f"{idx}. {product}")

            while True:
                try:
                    product_number = int(input("Enter product number to add to the order (or 0 to finish): "))
                    if product_number == 0:
                        break

                    if product_number < 1 or product_number > len(active_products):
                        print("Invalid product number. Please try again.")
                        continue

                    product = active_products[product_number - 1]
                    quantity = int(input(f"Enter quantity for {product.name}: "))

                    if quantity <= 0:
                        print("Quantity must be greater than 0. Please try again.")
                        continue

                    shopping_list.append((product, quantity))
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            try:
                if shopping_list:
                    total_price = store.order(shopping_list)
                    print(f"\nOrder successful! Total price: {total_price} dollars.")
                else:
                    print("No products selected for the order.")
            except Exception as e:
                print(f"Error while making the order: {e}")

        elif choice == "4":
            print("\nThank you for visiting the store. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=120),
        LimitedProduct("Shipping Fee", price=10, quantity=1, max_per_order=1)
    ]

    discount_percent = PercentageDiscountPromotion("30% off", 30)
    second_half_price = SecondItemHalfPricePromotion()
    third_one_free = Buy2Get1FreePromotion()

    product_list[0].set_promotion(discount_percent)  # 30% off
    product_list[1].set_promotion(second_half_price)  # second item 50%
    product_list[2].set_promotion(third_one_free)  # buy 2, get 1 for free

    store = Store(product_list)
    start(store)

    for product in product_list:
        print(product)
