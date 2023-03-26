from storage_for_view import Storage


class Store(Storage):
    def __init__(self, items: dict[str, int], capacity: int = 100):
        super().__init__(items, capacity)
