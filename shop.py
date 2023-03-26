from store import Store
from exceptions import TooManyDifferentProducts


class Shop(Store):
    def __init__(self, items: dict[str, int], capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, title: str, amount: int) -> None:
        if self.get_unique_items_count() >= 5:
            raise TooManyDifferentProducts

        super().add(title, amount)
