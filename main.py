from shop import Shop
from store import Store
from request import Request
from exceptions import BaseError

store = Store(items={"печеньки": 3, "собачки": 4, "коробки": 5})
shop = Shop(items={"собачки": 2, "печеньки": 5})
storages = {"магазин": shop, "склад": store}


def main():
    while True:
        # вывод содержимого на складе и в магазине
        for storage_name in storages:
            print(f"\nВ {storage_name} храниться:")
            items = storages[storage_name].get_items()
            for k, v in items.items():
                print(f'{v} {k}')

        # получение запроса от покупателя
        print('\nЕсли хотите закончить напишите "завершить"\n'
              'Введите запрос в формате: "Доставить 3 печеньки из склад в магазин"')
        customer_input = input('Ваш запрос: ')
        print()
        if 'завершить' in customer_input:
            break

        try:
            request = Request(req_str=customer_input, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        # выполнение действие с указанным товаром
        try:
            if request.departure == 'склад' and request.destination == 'магазин':
                store.remove(title=request.product, amount=request.amount)
                print(f'Курьер забрал {request.amount} {request.product} со {request.departure}')
                print(f'Курьер везет {request.amount} {request.product} со {request.departure} в {request.destination}')
                shop.add(title=request.product, amount=request.amount)
                print(f'Курьер доставил {request.amount} {request.product} в {request.destination}')

            elif request.departure == 'магазин' and request.destination == 'склад':
                shop.remove(title=request.product, amount=request.amount)
                print(f'Курьер забрал {request.amount} {request.product} со {request.departure}')
                print(f'Курьер везет {request.amount} {request.product} со {request.departure} в {request.destination}')
                store.add(title=request.product, amount=request.amount)
                print(f'Курьер доставил {request.amount} {request.product} в {request.destination}')
        except BaseError as error:
            print(error.message)


if __name__ == '__main__':
    main()
