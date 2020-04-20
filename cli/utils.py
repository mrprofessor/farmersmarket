from marketservice.seed import products


def validate_products(input_product_list, marketservice_obj):
    """ Identify products that are not in seed """

    acutal_product_list = [product.code for product in marketservice_obj.product_list]

    non_existent_products = [
        item for item in input_product_list if item not in acutal_product_list
    ]

    return non_existent_products


def print_basket(marketservice_obj, basket_items):
    """ Checkout and print basket """
    basket = marketservice_obj.checkout(basket_items)

    if not basket:
        return "No items yet"

    output_str = f"Item \t\t  Price\n"
    output_str += f"---- \t\t  -----\n"
    for item in basket.basket_items:
        output_str += f"{item.product.code} \t\t  {item.product.price}\n"
        if item.coupon:
            output_str += f"\t {item.coupon.name} \t -{item.discount}\n"

    output_str += f"------------------------\n"
    output_str += f"Total: \t\t  {basket.total()}"
    # print("Total: ", "\t", "{:.2f}".format(basket.total()))

    return output_str
