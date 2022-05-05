import random
import re
"""5. Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число).
Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод первого вхождения,
вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345."""

def file_creator(filename, pattern=None):
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
    
    def file_reader(file, pattern=None):
        file_text = file.read()
        if pattern:
            print(re.search(pattern, file_text).group(0))
            print(re.findall(pattern, file_text))
            new_file_text = re.sub(pattern, ' test_ex ', file_text)
            file.seek(0)
            file.truncate(0)
            file.write(new_file_text)
            file.seek(0)
            for line in file.readlines():
                print(line, end='')
            print(re.findall(' \w+ ', new_file_text))
        else:
            print(file_text)
    
    with open(f'{filename}.txt', 'w+', encoding='utf-8') as f:
        for i in final_list:
            f.write(f'{i[0]} {i[1]}\n')
    
    with open(f'{filename}.txt', 'r+', encoding='utf-8') as f:
        file_reader(f, pattern)
    
    
    
if __name__ == '__main__':
    file_creator('test_file', pattern='example345')