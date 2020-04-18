from unittest import TestCase
from marketservice.models import Product, Basket, BasketItem, Coupon


class TestMarketService(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_basket_to_dict(self):
        # Create two test products
        p1 = Product(name="Tea", code="TE", price=20.75)
        p2 = Product(name="Coffee", code="CF", price=10.50)

        # Create two coupons
        c1 = Coupon(name="BOGO", description="Buy one get one")
        c2 = Coupon(name="BTGT", description="Buy two get two")

        # Two basket items
        b1 = BasketItem(p1, c1, discount="3.50", should_apply="False")
        b2 = BasketItem(p2, c2, discount="1.75", should_apply="False")

        basket = Basket(items=[b1, b2])

        actual = basket.to_dict()
        expected = [
            {
                "product": {"name": "Tea", "code": "TE", "price": 20.75},
                "coupon": {"name": "BOGO", "description": "Buy one get one"},
                "discount": "3.50",
                "should_apply": "False",
            },
            {
                "product": {"name": "Coffee", "code": "CF", "price": 10.5},
                "coupon": {"name": "BTGT", "description": "Buy two get two"},
                "discount": "1.75",
                "should_apply": "False",
            },
        ]

        self.assertEqual(expected, actual)
