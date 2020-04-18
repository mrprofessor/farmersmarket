from typing import List
import json


class Product:
    def __init__(self, name: str, code: str, price: float):
        self.name = name
        self.code = code
        self.price = price


class Coupon:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description


class BasketItem:
    def __init__(
        self,
        product: Product,
        coupon: Coupon = None,
        discount: float = 0.00,
        should_apply: bool = True,
    ):
        self.product = product
        self.coupon = coupon
        self.discount = discount
        self.should_apply = should_apply


class Basket:
    def __init__(self, items: List[BasketItem] = None):
        self.basket_items = items

    def to_dict(self):
        return json.loads(json.dumps(self.basket_items, default=lambda x: x.__dict__))
