print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

score_3, score_4, score_5 = 0, 0, 0
student = int(input('Сколько человек в классе? '))

for _ in range(student):
    score = int(input('Введите оценку: '))
    if score == 5:
        score_5 += 1
    elif score == 4:
        score_4 += 1
    else:
        score_3 += 1
print('В классе', student, 'уч. Из них отл:', score_5, 'хор:', score_4, 'посредств:', score_3)

if (score_5 == score_4) or (score_5 == score_3) or (score_4 == score_3):
    if score_5 == score_4:
        print('Больше всего отличников и хорошистов:', score_5)
    #    score_54 = score_5
    if score_5 == score_3:
        print('Больше всего отличников и посредственных:', score_5)
    #    score_53 = score_5
    if score_4 == score_3:
        print('Больше всего хорошистов и посредственных:', score_4)
    #    score_43 = score_4
else:
    if score_5 > score_4 and score_5 > score_3:
        print('Больше всего отличников:', score_5)
    elif score_4 > score_3:
        print('Больше всего хорошистов:', score_4)
    else:
        print('Больше всего посредственных:', score_3)
        