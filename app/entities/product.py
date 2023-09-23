# coding: utf-8
"""Class to represent a product and product line entities."""

from pydantic import BaseModel


class Product(BaseModel):
    """Class representing product."""

    reference: str
    name: str
    price: float


class ProductLine(BaseModel):
    """Class representing product."""

    item: Product
    quantity: int = 1
