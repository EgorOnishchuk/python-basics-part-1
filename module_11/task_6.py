"""
В рамках разработки шахматного ИИ стоит новая задача: по заданным вещественным координатам коня и точки программа должна
определить, может ли конь ходить в эту точку. Используйте как можно меньше конструкций if и логических операторов.
Обеспечьте контроль ввода.

Пример:

Введите местоположение коня:

0.071

0.118

Введите местоположение точки на доске:

0.213

0.068

Конь в клетке (0, 1). Точка в клетке (2, 0).

Да, конь может ходить в эту точку.
"""

print('Задача 6. Ход конём')

while not (
    (0 <= (knight_x_coordinate := int(float(input('Введите координату x коня >>> ')) * 10)) <= 7) and
    (0 <= (knight_y_coordinate := int(float(input('Введите координату y коня >>> ')) * 10)) <= 7) and
    (0 <= (move_x_coordinate := int(float(input('Введите координату x хода коня >>> ')) * 10)) <= 7) and
    (0 <= (move_y_coordinate := int(float(input('Введите координату y хода коня >>> ')) * 10)) <= 7)
):
    print('Координаты введены неверно.')

print(f'Конь в клетке ({knight_x_coordinate}, {knight_y_coordinate}). '
      f'Точка в клетке ({move_x_coordinate}, {move_y_coordinate}).')

if (
    (abs(knight_x_coordinate - move_x_coordinate) == 1 and abs(knight_y_coordinate - move_y_coordinate) == 2) or
    (abs(knight_x_coordinate - move_x_coordinate) == 2 and abs(knight_y_coordinate - move_y_coordinate) == 1)
):
    print('Конь может ходить в эту точку.')
else:
    print('Конь не может ходить в эту точку.')
