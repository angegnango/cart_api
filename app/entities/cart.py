# coding: utf-8
"""Class to represent a cart entities."""

from dataclasses import dataclass
from app.abstractions.storage import CartStorage


@dataclass
class Cart:
    """Class representing a cart."""

    storage: CartStorage
    total: float = 0.0
    amount: float = 0.0
    discount: float = 0.0
