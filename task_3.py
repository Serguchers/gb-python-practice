"""3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным."""

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price

class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)
    
    def get_parent_data(self):
        print(f'Наименование: {self.get_name()}, цена: {self.get_price()} руб.')
        

if __name__ == '__main__':
    test_product = ItemDiscountReport('Молоко', 1000)
    test_product.get_parent_data()