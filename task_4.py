import random
"""4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции."""


def file_creator(filename):
    try:
        file = open(f'{filename}.txt')
    except:
        print(f'Создан файл {filename}.txt')
            
    else:
        print(f'{filename}.txt уже существует')
        file.close()
    
    List_to_write_1 = ['example345' if i % 10 == 0 else chr(random.randint(65, 90)) * 5 for i in range(100)]
    List_to_write_2 = [random.randint(1, 100) for _ in range(100)]
    final_list = list(zip(List_to_write_1, List_to_write_2))
    
    def file_reader(file):
        for i in file.readlines():
            print(i, end='')
        
    
    with open(f'{filename}.txt', 'w+', encoding='utf-8') as f:
        for i in final_list:
            f.write(f'{i[0]} {i[1]}\n')
    
    with open(f'{filename}.txt', 'r', encoding='utf-8') as f:
        file_reader(f)
    
    
    
if __name__ == '__main__':
    file_creator('test_file')