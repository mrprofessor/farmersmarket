from typing import List
from .models import Product, Coupon, BasketItem, Basket
from .seed import products as products_seed, coupons as coupons_seed


class MarketService:
    def __init__(self):
        self.product_list, self.coupon_list = self.seed()
        self.basket = None

    def seed(self):
        """ Create a list of products and coupons """
        product_list = [Product(**item) for item in products_seed]
        coupon_list = [Coupon(**item) for item in coupons_seed]
        return product_list, coupon_list

    def build_basket(self, basket_items: List[str]):
        """ Create the cart from the input list of items """
        b_items = []
        for b_item in basket_items:
            relevant_product = MarketService.search_item(
                key="code", value=b_item, search_list=self.product_list
            )
            b_items.append(BasketItem(product=relevant_product))
        self.basket = Basket(items=b_items)

    def calculate_invoice(self):
        """ Calculate the final invoice """
        if not self.basket:
            print("No items yet")
            return
        total = 0.00
        for item in self.basket.basket_items:
            print(item.product.code, "\t\t", item.product.price)
            total += item.product.price
            if item.coupon:
                print("\t", item.coupon.name, "\t", -item.discount)
                total -= item.discount
        print("Total: ", "\t", total)

    def apply_coupons(self):
        """ Apply all the coupons on the basket """
        for coupon in self.coupon_list:
            if coupon.name == "BOGO":
                self.apply_bogo(coupon)
            if coupon.name == "APPL":
                self.apply_appl(coupon)
            if coupon.name == "CHMK":
                self.apply_chmk(coupon)
            if coupon.name == "APOM":
                self.apply_apom(coupon)

    def apply_apom(self, coupon_obj):
        """
            Apply APOM coupon
            description: Purchase a bag of Oatmeal and get 50% off a bag of Apples
        """
        apples_without_coupons = [
            item
            for item in self.basket.basket_items
            if item.product.code == "AP1" and item.should_apply
        ]

        for item in self.basket.basket_items:
            # set the coupon should_apply flag false
            if item.product.code == "OM1" and item.should_apply:
                item.should_apply = False

                # Add discount to the apple
                discounted_apple = apples_without_coupons.pop()
                discounted_apple.should_apply = False
                discounted_apple.coupon = coupon_obj
                discounted_apple.discount = MarketService.calculate_discount_amount(
                    initial_price=discounted_apple.product.price,
                    discount_type="percent",
                    number=50,
                )

    def apply_chmk(self, coupon_obj):
        """
            Apply CHMK coupon
            description: Purchase a box of Chai and get milk free. (Limit 1).
        """
        milks = [
            item
            for item in self.basket.basket_items
            if item.product.code == "MK1" and item.should_apply
        ]
        if not len(milks):
            return

        # Set flag to check if once applied already
        once_applied = False
        for item in self.basket.basket_items:
            # set the coupon should_apply flag false
            if item.product.code == "CH1" and item.should_apply and not once_applied:
                item.should_apply = False
                once_applied = True

                # Add discount to the apple
                discounted_milk = milks.pop()
                discounted_milk.should_apply = False
                discounted_milk.coupon = coupon_obj
                discounted_milk.discount = MarketService.calculate_discount_amount(
                    initial_price=discounted_milk.product.price,
                    discount_type="percent",
                    number=100,
                )
            elif item.product.code == "CH1" and once_applied:
                item.should_apply = False

    def apply_appl(self, coupon_obj):
        """
            Apply APPL coupon
            description: If you buy 3 or more bags of Apples, the price drops to $4.50.
        """
        apples = [
            item for item in self.basket.basket_items if item.product.code == "AP1"
        ]
        # If there are less than 3 apples then the coupon doesn't apply
        if len(apples) < 3:
            return

        # TODO
        # Optimize later
        for item in self.basket.basket_items:
            # set the coupon should_apply flag false
            if item.product.code == "AP1" and item.should_apply:
                item.should_apply = False
                item.coupon = coupon_obj
                item.discount = MarketService.calculate_discount_amount(
                    initial_price=item.product.price, discount_type="fixed", number=4.50
                )

    def apply_bogo(self, coupon_obj):
        """
            Apply BOGO coupon
            description: Buy-One-Get-One-Free Special on Coffee. (Unlimited)
        """
        coffees_without_discount = [
            item
            for item in self.basket.basket_items
            if item.product.code == "CF1" and item.should_apply
        ]
        if not len(coffees_without_discount):
            return
        for item in self.basket.basket_items:
            # set the coupon should_apply flag false
            if item.product.code == "CF1" and item.should_apply:
                item.should_apply = False

                # Add discount to coffees
                discounted_coffee = coffees_without_discount.pop()
                discounted_coffee.should_apply = False
                discounted_coffee.coupon = coupon_obj
                discounted_coffee.discount = MarketService.calculate_discount_amount(
                    initial_price=discounted_coffee.product.price,
                    discount_type="percent",
                    number=100,
                )

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


ms = MarketService()
# ms.build_basket(basket_items=["CF1", "CH1", "AP1", "AP1", "AP1", "MK1"])
# ms.build_basket(basket_items=["CF1", "CF1", "CF1", "AP1"])
# ms.build_basket(basket_items=["CF1", "CH1", "CH1", "AP1"])
# ms.build_basket(basket_items=["CF1", "CH1", "CH1", "AP1", "OM1"])

# 1.
# ms.build_basket(basket_items=["CH1", "AP1", "CF1", "MK1"])
# 2.
# ms.build_basket(basket_items=["MK1", "AP1"])
# 3.
# ms.build_basket(basket_items=["CF1", "CF1"])
# 4.
ms.build_basket(basket_items=["AP1", "AP1", "CH1", "AP1"])
ms.apply_coupons()
ms.calculate_invoice()


"""


```
Basket: CH1, AP1, CF1, MK1
Total price expected: $20.34
```

```
Basket: MK1, AP1
Total price expected: $10.75
```

```
Basket: CF1, CF1
Total price expected: $11.23
```

```
Basket: AP1, AP1, CH1, AP1
Total price expected: $16.61
```
"""
