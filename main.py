from products import Product
from store import Store


if __name__ == "__main__":
    product_list = [Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    Product("MacBook Air M2", price=1450, quantity=100)]

    store = Store(product_list)

    active_products = store.get_all_products()
    for product in active_products:
        print(product.show())

    print("Total quantity in store:", store.get_total_quantity())

    try:
        price = store.order([(product_list[0], 1), (product_list[1], 2)])
        print(f"Order cost: {price} dollars.")
    except Exception as e:
        print(e)
