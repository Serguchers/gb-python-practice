"""1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
Проверить работу программы, создав экземпляр (объект) родительского класса."""

class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        super().__init__(name, price)
    
    def get_parent_data(self):
        print(f'Наименование: {self.name}, цена: {self.price} руб.')
        

if __name__ == '__main__':
    test = ItemDiscount('test_product', 123)
    test_product = ItemDiscountReport('Молоко', 1000)
    test_product.get_parent_data()