import pytest
from Product import *


@pytest.mark.parametrize('name', 'price', [('milk', 50.0), ('bread', 50.0), ('cookies', 100.0)])
def test_name_price(name: str, price: float):
    product = Product(name, price)
    assert product.name == name
    assert product.price == price


@pytest.mark.parametrize('productClass', 'productPrice', [([Product('milk', 50.0), Product('bread', 50.0)], Product('cookies', 100.0), 'product add')])
def test_add(productClass: Product, productPrice: str):
    basket_1 = Basket()
    for p in productClass:
        basket_1.add(p)
        assert productPrice == basket_1.add(p)


@pytest.mark.parametrize('productClass', 'productPrice', [([Product('milk', 50.0), Product('bread', 50.0)], Product('cookies', 100.0), 'product remove')])
def test_remove(productClass: Product, productPrice: str):
    basket_2 = Basket()
    for p in productClass:
        basket_2.remove(p)
        assert productPrice == basket_2.remove(p)


@pytest.mark.parametrize('productClass', 'productPrice', [([Product('milk', 50.0), Product('bread', 50.0)], Product('cookies', 100.0), 200)])
def test_summary(productClass: Product, productPrice: float):
    basket_3 = Basket()
    for p in productClass:
        basket_3.add(p)
    assert productPrice == basket_3.count_summary()

