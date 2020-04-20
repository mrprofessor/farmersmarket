import click
from marketservice.services import MarketService
from marketservice.models import Product, Coupon
from marketservice.seed import products as products_seed, coupons as coupons_seed

from .utils import validate_products, print_basket


@click.command()
@click.option(
    "--products",
    prompt="Enter product codes",
    help="List of space separated product codes in the basket",
)
@click.pass_context
def cli(ctx, products):
    product_list = [product for product in products.split(" ") if product != ""]
    non_existent_products = validate_products(product_list, ctx.obj["marketservice"])
    if non_existent_products:
        click.secho(
            f"Invalid product codes: {non_existent_products}\nExiting program!",
            blink=True,
            bold=True,
            fg="red",
        )
        return

    basket = print_basket(ctx.obj["marketservice"], product_list)
    click.secho(basket, fg="green", bold=True)


def seed_data():
    product_list = [Product(**item) for item in products_seed]
    coupon_list = [Coupon(**item) for item in coupons_seed]
    return MarketService(product_list, coupon_list)


def main():
    # click.clear()
    marketservice = seed_data()
    cli(obj={"marketservice": marketservice})
