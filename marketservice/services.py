from typing import List
from .models import Product, Coupon, BasketItem, Basket


class MarketService:
    def __init__(self, product_list: List[Product], coupon_list: List[Coupon]):
        self.product_list = product_list
        self.coupon_list = coupon_list

    def checkout(self, basket_items: List[str]):
        basket = self.build_basket(basket_items)
        self.apply_coupons(basket)
        return basket

    def build_basket(self, basket_items: List[str]):
        """ Create the cart from the input list of items """
        b_items = []
        for b_item in basket_items:
            relevant_product = MarketService.search_item(
                key="code", value=b_item, search_list=self.product_list
            )
            b_items.append(BasketItem(product=relevant_product))
        basket = Basket(items=b_items)
        return basket

    def apply_coupons(self, basket: Basket):
        """ Apply all the coupons on the basket """
        for coupon in self.coupon_list:
            # Target products with no coupons applied to them
            target_products_without_discount = [
                b_item
                for b_item in basket.basket_items
                if b_item.product.code == coupon.target and b_item.should_apply
            ]

            # Check whether the products satisfies the trigger limit of the
            # coupon
            if len(target_products_without_discount) < coupon.trigger_limit:
                continue
            if coupon.apply_all:
                self.__apply_on_all(coupon, basket)
            else:
                self.__appply_with_conditions(coupon, basket)

    def __apply_on_all(self, coupon: Coupon, basket: Basket):
        """ Apply on all the items """

        if coupon.apply_all:
            for item in basket.basket_items:
                if item.product.code == coupon.apply_on:
                    item.should_apply = False
                    item.coupon = coupon
                    item.discount = MarketService.calculate_discount_amount(
                        initial_price=item.product.price,
                        discount_type=coupon.discount_type,
                        number=coupon.discount,
                    )

    def __appply_with_conditions(self, coupon: Coupon, basket: Basket):
        """ Apply on items that satisfy the conditions such as limit """

        # Register a counter for limit
        applied_counter = 0
        # Applicable products with no coupons applied to them
        applicable_products_without_discount = [
            b_item
            for b_item in basket.basket_items
            if b_item.product.code == coupon.apply_on and b_item.should_apply
        ]

        # Iterate and apply
        for item in basket.basket_items:
            # Set the item should_apply flag false
            if item.product.code == coupon.target and item.should_apply:
                item.should_apply = False
                applied_counter += 1
                # Remove from the applicable products if target and
                # applicable are the same product
                if coupon.target == coupon.apply_on:
                    applicable_products_without_discount.remove(item)

                # Add discount to the product
                if applicable_products_without_discount:
                    discounted_product = applicable_products_without_discount.pop()
                    discounted_product.should_apply = False
                    discounted_product.coupon = coupon
                    discounted_product.discount = MarketService.calculate_discount_amount(
                        initial_price=discounted_product.product.price,
                        discount_type=coupon.discount_type,
                        number=coupon.discount,
                    )

            if coupon.limit > 0 and applied_counter == coupon.limit:
                return

    @staticmethod
    def calculate_discount_amount(
        initial_price: float, discount_type: str, number: float
    ):
        if discount_type == "percent":
            return initial_price * (number / 100)
        elif discount_type == "fixed":
            return initial_price - number

    @staticmethod
    def search_item(key: str, value, search_list):
        for item in search_list:
            if getattr(item, key) == value:
                return item
        return None
