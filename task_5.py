"""5. Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка), и перегрузку метода str дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса)."""

class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def set_price(self, value):
        self.__dict__[f'_{self.__class__.__base__.__name__}__price'] = value
    

class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount
        
    def get_parent_data(self):
        print(f'Наименование: {self.get_name()}, цена: {self.get_price()} руб.')
    
    def __str__(self) -> str:
        return f'Цена товара со скидкой: {self.get_price() * (1 - self.discount / 100)}'
    

        

if __name__ == '__main__':
    test_product = ItemDiscountReport('Молоко', 1000, 10)
    test_product.get_parent_data()
    print(test_product)