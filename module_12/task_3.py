"""
Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные
арифметические действия. Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его
цифр, максимальную или минимальную цифру. Каждое действие оформите в виде отдельной функции, а основную программу
зациклите.

Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.
"""

print('Задача 3. Апгрейд калькулятора')


def summarize_digits(number: int) -> int:
    """
    Суммирует цифры числа number.

    :param number: Число, цифры которого необходимо суммировать.
    :return: Сумма цифр.
    """
    sum_ = 0
    
    for digit in str(number):
        sum_ += int(digit)
    
    return sum_


def get_minimal_digit(number: int) -> int:
    """
    Определяет минимальную цифру числа number.
    :param number: Число, минимальную цифру которого необходимо найти.
    :return: Минимальная цифра.
    """
    minimal_digit = float('inf')
    
    for digit in str(number):
        digit = int(digit)
        if digit < minimal_digit:
            minimal_digit = digit
    
    return minimal_digit


def get_maximal_digit(number: int) -> int:
    """
    Определяет максимальную цифру числа number.
    :param number: Число, максимальную цифру которого необходимо найти.
    :return: Максимальная цифра.
    """
    maximal_digit = 0
    
    for digit in str(number):
        digit = int(digit)
        if digit > maximal_digit:
            maximal_digit = digit
    
    return maximal_digit


is_running = True
while is_running:
    if (action := input('Действия\n1 — суммирование цифр\n2 — минимальная цифра\n3 — максимальная цифра\n4 — выход\n'
                       'Введите действие >>> ')) == '1':
        print(f'Сумма цифр: {summarize_digits(int(input('Введите число >>> ')))}.')
    elif action == '2':
        print(f'Минимальная цифра: {get_minimal_digit(int(input('Введите число >>> ')))}.')
    elif action == '3':
        print(f'Максимальная цифра: {get_maximal_digit(int(input('Введите число >>> ')))}.')
    elif action == '4':
        is_running = False
    else:
        print('Действие введено неверно.')
