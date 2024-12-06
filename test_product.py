import pytest
from products import Product

# Test that creating a normal product works.

def test_product():
    product = Product(name="Laptop", price=1200.99, quantity=10)

    assert product.name == "Laptop", "Product name should be 'Laptop'"
    assert product.price == 1200.99, "Product price should be 1200.99"
    assert product.quantity == 10, "Product quantity should be 10"


# Test that creating a product with invalid details
# (empty name, negative price) invokes an exception.

# def test_product_error():
#     product = Product(name="Laptop", price=1200.99, quantity=10)
#
#     assert product.name == "", "Product name should be 'Laptop'"
#     assert product.price == 1200.99, "Product name should be 1200.99"
#     assert product.quantity == 0, "Product name should be 10"


# Test that when a product reaches 0 quantity, it becomes inactive.

# def test_buy():
#     product = Product(name="Laptop", price=1200.99, quantity=5)
#     product.buy(5)
#
#     assert product.quantity == 0
#     assert product.deactivate


# Test that product purchase modifies the quantity and returns the right output.
def test_buy():
    product = Product(name="Laptop", price=1200.99, quantity=10)

    total_price = product.buy(3)

    assert product.quantity == 7
    assert total_price == 1200.99 * 3
    assert product.active
    # product_info = product.show()
    print(product.show())
    print(round(total_price, 2))
    print(product.is_active())
    # print(f"Total price for 4 units: {round(total_price, 2)}")


# Test that buying a larger quantity than exists invokes exception.
# def test_quantity():
#     product = Product(name="Laptop", price=1200.99, quantity=10)
#
#     try:
#         product.buy(11)
#         assert False, "Expected ValueError was not raised"
#     except ValueError as e:
#         assert str(e) == "Insufficient product in stock."
#
#     assert product.quantity == 10
