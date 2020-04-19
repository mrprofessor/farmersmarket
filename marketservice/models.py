from typing import List, Union
import json


class Product:
    def __init__(self, name: str, code: str, price: float):
        self.name = name
        self.code = code
        self.price = price


# Breakdown coupon's description into quantifiable attributes
# For example: BOGO on coffee can be translated as an object
# with certain properties should look like
# bogo_obj.target = "CF1"
# bogo_obj.apply_on = "CF1"
# bogo_obj.discount = 100
# bogo_obj.discount_type = "percent"
# bogo_obj.trigger_limit = 1
# bogo_obj.limit = 0 # no limit
# bogo_obj.apply_all = False
class Coupon:
    def __init__(
        self,
        name: str,
        description: str,
        target: str,
        apply_on: str,
        discount: float,
        discount_type: Union["percent", "fixed"],
        trigger_limit: int,
        limit: int,
        apply_all: bool,
    ):
        self.name = name
        self.description = description
        self.target = target
        self.apply_on = apply_on
        self.discount = discount
        self.discount_type = discount_type
        self.trigger_limit = trigger_limit
        self.limit = limit
        self.apply_all = apply_all


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
        return {
            "basket_items": json.loads(
                json.dumps(self.basket_items, default=lambda x: x.__dict__)
            ),
            "total": self.total(),
        }

    def total(self):
        total = 0.00
        for item in self.basket_items:
            total += item.product.price
            total -= item.discount
        return round(total, 2)
