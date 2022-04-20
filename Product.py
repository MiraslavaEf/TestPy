from typing import List


class Product:
    name: str
    price: float

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Basket:

    def __init__(self):
        self.basket: List[Product] = []

    def add(self, product: Product):
        self.basket.append(product)
        return 'add'

    def remove(self, product: Product):
        self.basket.remove(product)
        return 'remove'

    def count_sum(self):
        summary = 0
        for i in range(0, len(self.basket)):
            summary += self.basket[i].price
        return summary


milk = Product('milk', 50.0)
bread = Product('bread', 50.0)
cookies = Product('cookies', 100.0)

# basket1 = Basket()
# print(basket1.add(milk))
# print(basket1.add(bread))
# print(basket1.add(cookies))
# print(basket1.count_sum())