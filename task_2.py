import os
import sys

def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.
    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    os.chdir(sPath)
    for i in os.listdir():
        if os.path.isdir(i):
            print(os.getcwd(), i)
            print_directory_contents(i)
        else:
            print(os.getcwd(), i)
    os.chdir('..')


if __name__ == '__main__':
    print_directory_contents(sys.argv[1])