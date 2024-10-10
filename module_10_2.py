from threading import Thread
from time import sleep


class Knight(Thread):
    # name = ''
    # power = 0
    def __init__(self, name_, power):
        self.name_ = name_
        self.power = power
        super().__init__()
        # print(f'name_ - {self.name_}')

    def run(self):
        animy = 100
        print(f'{self.name_}, на нас напали!')
        pow_of_kn = 0
        days = 0
        # print(f'aminy 1 - {animy}')
        while animy - pow_of_kn > 0:
            sleep(1)
            days += 1
            # print(f'aminy 2 - {pow_of_kn}')
            # pow_of_kn += self.power
            pow_of_kn += self.power
            print(f'{self.name_} сражается {days} дней, осталось {animy - pow_of_kn} воинов.')
            # print(' ')
        print(f'{self.name_} одержал победу спустя {days} дней(дня)!')

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
