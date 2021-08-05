print('Задача 7. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль
#среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

start = int(input('Число a: '))
finish = int(input('Число b: '))
fingerpanch = 0
summ = 0
for number in range(start, finish + 1):
    if number % 3 == 0:
        summ += number
        fingerpanch += 1
arithmetic_mean = summ / fingerpanch
print('Среднее ариметическое чисел из отрезка '
      '[' + str(start) + ';' + str(finish) + '], \nкоторые кратны числу 3, '
        'равно', arithmetic_mean)