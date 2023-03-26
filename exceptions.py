class BaseError(Exception):
    message = 'Неожиданная ошибка'


class NotEnoughSpace(BaseError):
    message = 'В магазин недостаточно места, попробуйте что-то другое'


class NotEnoughProduct(BaseError):
    message = 'Не хватает на складе, попробуйте заказать меньше'


class TooManyDifferentProducts(BaseError):
    message = 'Слишком много товаров'


class NoProductsWithThisName(BaseError):
    message = 'Такого товара нет на складе'


class InvalidRequest(BaseError):
    message = 'Неправильный запрос'


class InvalidStorageName(BaseError):
    message = 'Такого склада не существует'
