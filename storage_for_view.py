from abc import ABC
from exceptions import NotEnoughSpace, NoProductsWithThisName


class Storage(ABC):
    def __init__(self, items: dict[str, int], capacity: int):
        empty_products = [k for k, v in items.items() if v <= 0]
        for ep in empty_products:
            items.pop(ep)
        self.items = items
        self.capacity = capacity

    def add(self, title: str, amount: int) -> None:
        if self.capacity >= amount:
            if title in self.items.keys():
                self.items[title] += amount
            else:
                self.items[title] = amount
            self.capacity -= amount
        else:
            raise NotEnoughSpace

    def remove(self, title: str, amount: int) -> None:
        if title not in self.items.keys():
            raise NoProductsWithThisName

        if self.items.get(title, 0) - amount >= 0:
            self.items[title] -= amount
            self.capacity += amount

    def get_free_space(self) -> int:
        total = sum([self.items.values()])
        return self.capacity - total

    def get_items(self) -> dict:
        return self.items

    def get_unique_items_count(self) -> int:
        return len(self.items)

