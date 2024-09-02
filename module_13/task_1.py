"""
В прошлый раз учитель написал программу, которая выводит числа в формате плавающей точки, однако он вспомнил, что не
учёл одну важную вещь: числа-то могут идти от нуля.

Задано положительное число x (x > 0). Ваша задача — преобразовать его в формат плавающей точки, то есть
x = a * 10 ** b, где 1 ≤ а < 10. Обратите внимание, что x теперь больше нуля, а не больше единицы. Обеспечьте контроль
ввода.

Пример 1:

Введите число: 92345

Формат плавающей точки: x = 9.2345 * 10 ** 4

Пример 2:

Введите число: 0.0012

Формат плавающей точки: x = 1.2 * 10 ** -3
"""

from decimal import Decimal

print("Задача 1. Урок информатики 2")


def represent_as_exponential(number: int | float | Decimal) -> str | None:
    """
    Представляет число в экспоненциальной форме.

    :param number: Число, которое необходимо представить в экспоненциальной форме.
    :return: Экспоненциальная запись формата "число = мантисса * 10 ** экспонента".
    """
    initial_number = number
    exponent = 0

    if 0 < number < 1:
        while number < 1:
            number *= 10
            exponent -= 1
    elif number >= 10:
        while number >= 10:
            number /= 10
            exponent += 1

    return f"{initial_number} = {number} * 10 ** {exponent}"


NUMBER = float(input("Введите положительное число: "))
EXPONENTIAL_FORM = represent_as_exponential(NUMBER)
print(
    "Формат плавающей точки: "
    f"{EXPONENTIAL_FORM if EXPONENTIAL_FORM is not None else f'не определён для числа {NUMBER}'}."
)
