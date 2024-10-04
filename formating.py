# Использование %
from module_7_2 import result

team1_num = '5'
print('В команде Мастера кода участников: %s!' % team1_num)
team2_num = '6'
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

# Использование format():
score_2 = '42'
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
team1_time = str(18015.2)
print('Волшебники данных решили задачи за {} с !'.format(team1_time))

# Использование f-строк:
score_1 = '40'
print(f'Команды решили {score_1} и {score_2} задач.')
challenge_result = 'Мастера кода'
print((f'Результат битвы: победа команды {challenge_result}!'))
tasks_total = '82'
time_avg = str(350.4)
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')
print('-=-' * 11)

# Расчёты

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

# Использование format():
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} с !'.format(team1_time))

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print((f'Результат битвы: победа команды {challenge_result}!'))
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')