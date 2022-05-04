from pprint import pprint
import sys
import random

"""Разработать генератор случайных чисел. В функцию передавать начальное и конечное число
генерации (нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи
словаря должны создаваться по шаблону: “elem_<номер_элемента>”. Вывести содержимое
созданных списка и словаря."""


def rnd_gen(start, end):
    rnd_list = []
    rnd_dict = {}
    dict_counter = 1
    for i in range(10):
        number = random.randint(start, end)
        if number == 0:
            continue
        rnd_list.append(number)
        rnd_dict[f'elem_{dict_counter}'] = number
        dict_counter += 1
    
    return (rnd_dict, rnd_list)
        
        
if __name__ == '__main__':
    res = rnd_gen(int(sys.argv[1]), int(sys.argv[2]))
    print(res[0])
    print(res[1])