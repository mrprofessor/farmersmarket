from unittest import TestCase
from marketservice.models import Product, Basket, BasketItem, Coupon


class TestMarketService(TestCase):
    def setUp(self):
        # Create two test products
        self.p1 = Product(name="Tea", code="TE", price=20.75)
        self.p2 = Product(name="Coffee", code="CF", price=10.50)

        # Create two coupons
        self.c1 = Coupon(
            name="BOGO",
            description="Buy-One-Get-One-Free Special on Coffee. (Unlimited)",
            target="CF1",
            apply_on="CF1",
            discount=100,
            discount_type="percent",
            trigger_limit=1,
            limit=0,
            apply_all=False,
        )

        self.c2 = Coupon(
            name="APPL",
            description="If you buy 3 or more bags of Apples, the price drops to $4.50.",
            target="AP1",
            apply_on="AP1",
            discount=4.50,
            discount_type="fixed",
            trigger_limit=3,
            limit=0,
            apply_all=True,
        )

    def tearDown(self):
        pass

    def test_basket_total(self):
        # Two basket items
        b1 = BasketItem(self.p1, self.c1, discount=3.50, should_apply="False")
        b2 = BasketItem(self.p2, self.c2, discount=1.75, should_apply="False")

        basket = Basket(items=[b1, b2])

        actual = basket.total()
        expected = 26.00
        self.assertEqual(actual, expected)

    def test_basket_to_dict(self):
        # Two basket items
        b1 = BasketItem(self.p1, self.c1, discount=3.50, should_apply="False")
        b2 = BasketItem(self.p2, self.c2, discount=1.75, should_apply="False")

        basket = Basket(items=[b1, b2])

        actual = basket.to_dict()
        expected = {
            "basket_items": [
                {
                    "product": {"name": "Tea", "code": "TE", "price": 20.75},
                    "coupon": {
                        "name": "BOGO",
                        "description": "Buy-One-Get-One-Free Special on Coffee. (Unlimited)",
                        "target": "CF1",
                        "apply_on": "CF1",
                        "discount": 100,
                        "discount_type": "percent",
                        "trigger_limit": 1,
                        "limit": 0,
                        "apply_all": False,
                    },
                    "discount": 3.5,
                    "should_apply": "False",
                },
                {
                    "product": {"name": "Coffee", "code": "CF", "price": 10.5},
                    "coupon": {
                        "name": "APPL",
                        "description": "If you buy 3 or more bags of Apples, the price drops to $4.50.",
                        "target": "AP1",
                        "apply_on": "AP1",
                        "discount": 4.5,
                        "discount_type": "fixed",
                        "trigger_limit": 3,
                        "limit": 0,
                        "apply_all": True,
                    },
                    "discount": 1.75,
                    "should_apply": "False",
                },
            ],
            "total": 26.0,
        }

        self.assertEqual(expected, actual)
