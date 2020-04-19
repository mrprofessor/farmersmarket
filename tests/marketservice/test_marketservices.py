import types
from unittest import TestCase
from marketservice.services import MarketService


class TestMarketService(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calculate_discount_amount_percentage(self):
        actual = MarketService.calculate_discount_amount(
            initial_price=10.00, discount_type="percent", number=25
        )
        expected = 2.50
        self.assertEqual(expected, actual)

    def test_calculate_discount_amount_fixed(self):
        actual = MarketService.calculate_discount_amount(
            initial_price=10.00, discount_type="fixed", number=3.75
        )
        expected = 6.25
        self.assertEqual(expected, actual)

    def test_search_item(self):
        # create two test objects
        obj1 = types.SimpleNamespace(name="python")
        obj2 = types.SimpleNamespace(name="ruby")
        search_list = [obj1, obj2]

        actual = MarketService.search_item(
            key="name", value="python", search_list=search_list
        ).name
        expected = "python"
        self.assertEqual(expected, actual)

    def test_search_item_not_found(self):
        # create two test objects
        obj1 = types.SimpleNamespace(name="python")
        obj2 = types.SimpleNamespace(name="ruby")
        search_list = [obj1, obj2]

        actual = MarketService.search_item(
            key="name", value="java", search_list=search_list
        )
        expected = None
        self.assertEqual(expected, actual)
