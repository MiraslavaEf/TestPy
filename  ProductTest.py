import pytest
from Product import *


@pytest.mark.parametrize('name, price', [('water', 25.0 ), ('bread', 20.0), ('meat', 170.0)])
def test_name_price(name: str, price: float):
    product = Product(name, price)
    assert product.name == name
    assert product.price == price


@pytest.mark.parametrize('productClass, productPrice', [([Product('water', 25.0), Product('bread', 20.0)], Product('meat', 170.0), 'мы добавили продукт')])
def test_add(productClass: Product, productPrice: str):
    basket_1 = Basket()
    for p in productClass:
        basket_1.add(p)
        assert productPrice == basket_1.add(p)


@pytest.mark.parametrize('productClass, productPrice', [([Product('water', 25.0), Product('bread', 20.0)], Product('meat', 170.0), 'мы добавили продукт')])
def test_remove(productClass: Product, productPrice: str):
    basket_2 = Basket()
    for p in productClass:
        basket_2.add(p)
        assert productPrice == basket_2.add(p)


@pytest.mark.parametrize('productClass, productPrice', [([Product('water', 25.0), Product('bread', 20.0)], Product('meat', 170.0), 225)])
def test_sum(productClass: Product, productPrice: float):
    basket_3 = Basket()
    for p in productClass:
        basket_3.add(p)
    assert productPrice == basket_3.count_sum()

