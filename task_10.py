print('Задача 10.')

#Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# 
# Вводится число N,
# далее еще N − 1 чисел: 
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

number_n = int(input('Сколько всего должно быть карточек? '))
summ, card_count = 0, 0

for _ in range(1, number_n):
    number_card = int(input('Введите номер карточки: '))
    summ += number_card

for n_count in range(0, number_n + 1):
    card_count += n_count

number_x = card_count - summ
print('Номер потерянной карточки', number_x)