print('Задача 9. ...Теперь можно посчитать и свою')

# Пока бухгалтер считала среднюю зарплату сотрудников,
# ей стало интересно, а не зря ли она работает столько времени на одном месте?
# Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
# 
# Пользователь вводит 10 чисел.
# Напишите программу, которая проверяет, упорядочены ли они по возрастанию.

salary_old = 0
for _ in range(1, 11):
    salary = int(input('Введите свою зарплату за этот месяц: '))
    if salary > salary_old:
        print('Всё хорошо, зарплата увеличивается.')
    else:
        print('Зря работала...')
    salary_old = salary
#    print(salary_old)