import math
"""2. Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False."""

def is_int(number):
    if int(number) == number:
        print('Введено целое число.')
    else:
        print('Введено дробное число.')
        decimal_part, int_part = math.modf(number)
        number_position = 0
        while int_part !=0:
            int_part //= 10
            number_position +=1
        decimal_part *= 10 ** number_position
        decimal_part = round(decimal_part, 0)
        if int(number) == decimal_part:
            return True
        return False
        


if __name__ == '__main__':
    print(is_int(float(input())))