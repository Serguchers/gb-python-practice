"""4. Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего (функция,
отвечающая за отображение информации о товаре в одной строке)."""

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
    def __init__(self, name, price):
        super().__init__(name, price)
    
    def get_parent_data(self):
        print(f'Наименование: {self.get_name()}, цена: {self.get_price()} руб.')
    

        

if __name__ == '__main__':
    test_product = ItemDiscountReport('Молоко', 1000)
    test_product.get_parent_data()
    test_product.set_price(111011)
    test_product.get_parent_data()
    print(test_product.get_price())