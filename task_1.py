import sys
"""Написать функцию, реализующую вывод таблицы умножения размерностью AｘB. Первый и
второй множитель должны задаваться в виде аргументов функции. Значения каждой строки
таблицы должны быть представлены списком, который формируется в цикле. После этого
осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
Полученная строка выводится в главной функции. Элементы строки (элементы таблицы
умножения) должны разделяться табуляцией."""


str_builder = lambda my_l: [i for i in map(lambda el: '\t'.join(el), my_l)]

def main(a, b):
    def multiplication_func(a, b):
        res = []
        for i in range(1, a + 1):
            intm_res = []
            for j in range(1, b + 1):
                intm_res.append(str(i * j))
            res.append(intm_res)
                
        return res
    
    str_result = str_builder(multiplication_func(a, b))
    for i in str_result:
        print(i)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))