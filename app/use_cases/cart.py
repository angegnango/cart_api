# coding: utf-8
"""Module to add item to cart."""
from app.entities.cart import Cart
from app.abstractions.storage import CartStorage


def add_item_to_cart(product_line: dict, cart_storage: CartStorage):
    """."""
    cart = Cart(storage=cart_storage)
    cart.storage.add_item(product_line)
    cart_items = cart.storage.get_items()
    cart.total = sum(
        [
            product_line["item"]["price"] * product_line["quantity"]
            for product_line in cart_items
        ]
    )
    cart.amount = cart.total - (cart.total * cart.discount)
    return {
        "items": cart_items,
        "total": cart.total,
        "discount": cart.discount,
        "amount": cart.amount,
    }
