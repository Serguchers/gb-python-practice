import os
"""1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла,
а затем «выделение» из этого пути имени файла (без расширения)."""

def file_path(filename):
    abs_path = os.path.abspath(filename)
    return abs_path.split('\\')[-1].split('.')[0]
    
if __name__ == '__main__':
    print(file_path('task_1.py'))