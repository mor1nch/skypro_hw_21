from abc import ABC, abstractmethod
from exceptions import NotEnoughSpace, NoProductsWithThisName


class Storage(ABC):
    def __init__(self, items: dict[str, int], capacity: int):
        empty_products = [k for k, v in items.items() if v <= 0]
        for ep in empty_products:
            items.pop(ep)
        self.items = items
        self.capacity = capacity

    @abstractmethod
    def add(self, title: str, amount: int) -> None:
        if self.capacity >= amount:
            self.items[title] += amount
            self.capacity -= amount
        else:
            raise NotEnoughSpace

    @abstractmethod
    def remove(self, title: str, amount: int) -> None:
        if title not in self.items.keys():
            raise NoProductsWithThisName

        if self.items.get(title, 0) - amount > 0:
            self.items[title] -= amount
            self.capacity += amount

    @abstractmethod
    def get_free_space(self) -> int:
        total = sum([self.items.values()])
        return self.capacity - total

    @abstractmethod
    def get_items(self) -> dict[str, int]:
        return self.items

    @abstractmethod
    def get_unique_items_count(self) -> int:
        return len(self.items)
