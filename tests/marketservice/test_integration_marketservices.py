from unittest import TestCase
from marketservice.services import MarketService
from marketservice.models import Product, Coupon
from marketservice.seed import products as products_seed, coupons as coupons_seed


class TestMarketServiceIntegration(TestCase):
    def setUp(self):
        self.product_list = [Product(**item) for item in products_seed]
        self.coupon_list = [Coupon(**item) for item in coupons_seed]
        self.market_service = MarketService(self.product_list, self.coupon_list)

    def tearDown(self):
        pass

    def test_apply_case1(self):
        basket = self.market_service.checkout(
            basket_items=["CH1", "AP1", "AP1", "AP1", "MK1"]
        )
        expected = basket.total()
        actual = 16.61
        self.assertEqual(expected, actual)

    def test_apply_case2(self):
        basket = self.market_service.checkout(basket_items=["CH1", "AP1", "CF1", "MK1"])
        expected = basket.total()
        actual = 20.34
        self.assertEqual(expected, actual)

    def test_apply_case3(self):
        basket = self.market_service.checkout(basket_items=["MK1", "AP1"])
        expected = basket.total()
        actual = 10.75
        self.assertEqual(expected, actual)

    def test_apply_case4(self):
        basket = self.market_service.checkout(basket_items=["CF1", "CF1"])
        expected = basket.total()
        actual = 11.23
        self.assertEqual(expected, actual)

    def test_apply_case5(self):
        basket = self.market_service.checkout(basket_items=["AP1", "AP1", "CH1", "AP1"])
        expected = basket.total()
        actual = 16.61
        self.assertEqual(expected, actual)

    def test_apply_case6(self):
        basket = self.market_service.checkout(basket_items=["MK1", "CH1", "CH1", "MK1"])
        expected = basket.total()
        actual = 10.97
        self.assertEqual(expected, actual)

    def test_check_basket_items_length(self):
        basket = self.market_service.checkout(basket_items=["CH1", "MK1"])
        actual = basket.to_dict()
        self.assertEqual(len(actual["basket_items"]), 2)
