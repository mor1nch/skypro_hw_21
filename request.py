from storage_for_view import Storage
from exceptions import InvalidRequest, InvalidStorageName


class Request:
    def __init__(self, req_str: str, storages: dict[str, Storage]):
        req_str = req_str.lower().split()
        if len(req_str) != 7:
            raise InvalidRequest

        self.departure = req_str[4]
        self.destination = req_str[6]
        self.amount = int(req_str[1])
        self.product = req_str[2]

        if self.departure not in storages or self.destination not in storages:
            raise InvalidStorageName

    def __repr__(self):
        return f'from = {self.departure}' \
               f'to = {self.destination}' \
               f'amount = {self.amount}' \
               f'product = {self.product}'
