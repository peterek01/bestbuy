from products import Product, NonStockedProduct, LimitedProduct
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
            for product in store.get_all_products():
                print(product.show())
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
                print(f"{idx}. {product.show()}")

            while True:
                try:
                    product_number = int(input("Enter product number to add to the order (or 0 to finish): "))
                    if product_number == 0:
                        break

                    if product_number < 1 or product_number > len(active_products):
                        print("Invalid product number. Please try again.")
                        continue

                    product = active_products[product_number - 1]

                    while True:
                        try:
                            quantity = int(input(f"Enter quantity for {product.name}: "))

                            if quantity <= 0:
                                print("Quantity must be greater than 0. Please try again.")
                                continue

                            if isinstance(product, LimitedProduct) and quantity > product.max_per_order:
                                print(f"Cannot add more than {product.max_per_order} of {product.name}.")
                                continue

                            # Dodanie produktu do zamówienia, jeśli ilość jest poprawna
                            shopping_list.append((product, quantity))
                            break

                        except ValueError:
                            print("Invalid input. Please enter numbers only.")
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

store = Store(product_list)
start(store)
