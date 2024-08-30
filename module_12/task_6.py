"""
Напишите функцию, вычисляющую наибольший общий делитель двух чисел.
"""

print('Задача 6. НОД')


def get_greatest_common_divisor(number_1: int, number_2: int) -> int:
    """
    Вычисляет наибольший общий делитель (НОД) двух чисел.

    :param number_1: Первое число.
    :param number_2: Второе число.
    :return: Наибольший общий делитель.
    """
    while number_2 != 0:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1


print(f'Наибольший общий делитель: {get_greatest_common_divisor(
    int(input('Введите первое число >>> ')),
    int(input('Введите второе число >>> '))
)}.')
