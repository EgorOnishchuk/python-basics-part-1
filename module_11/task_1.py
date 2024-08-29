"""
При оплате покупок картой за рубежом банки делают конвертацию через промежуточную валюту. Например, если оплачивать
отечественной картой товар в евро, то сначала эта сумма конвертируется в доллары, а потом — в рубли.

Напишите программу, которая получает на вход стоимость покупки в евро, а затем выводит ответ в рублях. Представим, что
мы живём в альтернативной реальности, где 1 евро = 1.25 доллара, а 1 доллар = 60.87 руб.
"""

from decimal import Decimal

print('Задача 1. Конвертация')

CURRENCY = '€'
INPUT_TO_INTERMEDIATE = Decimal(1.25)
INTERMEDIATE_TO_OUTPUT = Decimal(60.87)
TRANSACTION = Decimal(input(f'Введите стоимость покупки, {CURRENCY} >>> '))

CONVERTED_TRANSACTION = round(TRANSACTION * INPUT_TO_INTERMEDIATE * INTERMEDIATE_TO_OUTPUT, 2)

print(f'Стоимость: {CONVERTED_TRANSACTION} ₽.')
