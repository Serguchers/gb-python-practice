"""2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения."""

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)
    
    def get_parent_data(self):
        print(f'Наименование: {self.__name}, цена: {self.__price} руб.')
        

if __name__ == '__main__':
    test_product = ItemDiscountReport('Молоко', 1000)
    test_product.get_parent_data()