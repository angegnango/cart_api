# coding: utf-8
"""."""

from typing import Dict, Any

from app.abstractions.storage import CartStorage


class InMemoryStorage(CartStorage):
    """."""

    datasource: Dict[str, Dict] = {}
    selector: str = ""

    @classmethod
    def init(self, dsn: str):
        """."""
        self.selector = dsn
        if self.selector not in self.datasource:
            self.datasource[self.selector] = {}

        return self

    @classmethod
    def add_item(self, data: Dict):
        """."""
        self.datasource[self.selector][data["item"]["reference"]] = data
        return self.datasource[self.selector]

    @classmethod
    def get_items(self):
        """."""
        return [item for item in self.datasource[self.selector].values()]


STORAGES: Dict[str, Any] = {"in_memory": InMemoryStorage}


def get_storage(dsn, type_storage="in_memory"):
    """."""
    return STORAGES.get(type_storage).init(dsn)
