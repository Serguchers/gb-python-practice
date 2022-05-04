"""6. Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса. Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами."""
from re import I


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
    

class ItemDiscountReportOne(ItemDiscount):
    def get_info(self):
        print(self.get_name())
        

class ItemDiscountReportTwo(ItemDiscount):
    def get_info(self):
        print(self.get_price())
        

if __name__ == '__main__':
    first_product = ItemDiscountReportOne('молоко', 1000)
    second_product = ItemDiscountReportTwo('сок', 3000)
    #1
    first_product.get_info()
    second_product.get_info()
    #2
    a = first_product.get_info
    b = second_product.get_info
    a()
    b()
    #3
    def info_caller(prod_obj):
        prod_obj.get_info()
        
    info_caller(first_product)
    info_caller(second_product)