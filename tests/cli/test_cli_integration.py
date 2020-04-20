from unittest import TestCase
from click.testing import CliRunner
from cli.app import cli


from marketservice.services import MarketService
from marketservice.models import Product, Coupon
from marketservice.seed import products as products_seed, coupons as coupons_seed


class TestCliIntegration(TestCase):
    def setUp(self):
        pass
        # self.product_list = [Product(**item) for item in products_seed]
        # self.coupon_list = [Coupon(**item) for item in coupons_seed]
        # self.market_service = MarketService(self.product_list, self.coupon_list)

    def tearDown(self):
        pass

    def test_cli_case1(self):
        runner = CliRunner()
        actual = runner.invoke(cli, ["--products", "CH1"])
        expected = "Item \t\t  Price\n---- \t\t  -----\nCH1 \t\t  3.11\n------------------------\nTotal: \t\t  3.11\n"
        self.assertEqual(actual.exit_code, 0)
        self.assertEqual(actual.output, expected)

    def test_cli_case2(self):
        runner = CliRunner()
        actual = runner.invoke(cli, ["--products", "CH1 MK1 CF1 CF1"])
        expected = "Item \t\t  Price\n---- \t\t  -----\nCH1 \t\t  3.11\nMK1 \t\t  4.75\n\t CHMK \t -4.75\nCF1 \t\t  11.23\nCF1 \t\t  11.23\n\t BOGO \t -11.23\n------------------------\nTotal: \t\t  14.34\n"
        self.assertEqual(actual.exit_code, 0)
        self.assertEqual(actual.output, expected)

    def test_cli_case3(self):
        runner = CliRunner()
        actual = runner.invoke(cli, ["--products", "CM1 CH1 ZK1"])
        expected = "Invalid product codes: ['CM1', 'ZK1']\nExiting program!\n"
        # breakpoint()
        self.assertEqual(actual.exit_code, 0)
        self.assertEqual(actual.output, expected)
