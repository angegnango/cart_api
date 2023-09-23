# coding: utf-8
"""Storage abstraction module."""

from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class CartStorage(ABC):  # pragma: no cover
    """Basic Storage abstration class."""

    @abstractmethod
    def init(self, dsn: str):
        """."""
        pass

    @abstractmethod
    def add_item(self, item: dict):
        """."""
        pass

    @abstractmethod
    def update_item(self, item_reference: str, quantity: int):
        """."""
        pass

    @abstractmethod
    def remove_item(self, item_reference: str):
        """."""
        pass

    @abstractmethod
    def get_items(self):
        """."""
        pass
