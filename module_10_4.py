from threading import Thread
import threading
from random import randint
from time import sleep
from queue import Queue

pers_queue_in = Queue()
table_queue = Queue()
threadsin = []
threads_table = []

def waiting(a=0, b=0, name=''):
    time_sleep = randint(a, b)

    for i in range(time_sleep):
        sleep(1)

class Table(Thread):
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest
        super().__init__()

    def table_for_service(guest=None):
        # Если идёт поиск свободного стола
        if guest != None:
            find_table = [inst for inst in tables if inst.guest == None]
            # Усаживаем за свободный стол гостя
            if find_table != []:
                # find_table[0].guest = guest
                t_out = str(find_table[0].number)
                #Первый свободный стола
                find_table[0].guest = guest
                guest_ = pers_queue_in.get()
                #Запуск потока на обслуживание стола Гостя
                print(f'    {find_table[0].guest} сел(-а) за стол номер {t_out}. ')
                thr_table = Thread(target=waiting(a=3, b=5, name=t_out), name=t_out)
                threads_table.append(thr_table)
                # Постановка гостя в очередь (вернее, гостя из очереди не исключаем
            else:
                print(f'Все столы заняты. {guest} - в очереди.')

    def table_after_service(table=None, guest=None):
        # Если идёт поиск свободного стола
        if table != None:
            find_table = [inst for inst in tables if inst.number == int(table)]
            if find_table != []:
                find_table[0].guest = guest
                t_out = str(find_table[0].number)
                #Первый свободный стол
                #Запуск потока на обслуживание стола Гостя
                print(f'     {find_table[0].guest} сел(-а) за стол номер  {find_table[0].number}.')
                thr_table = Thread(target=waiting(a=3, b=5, name=t_out), name=t_out)
                threads_table.append(thr_table)
                # Постановка стола в очередь
                cafe.discuss_guests()
            else:
                print(f'Все столы заняты. {guest} - в очереди.')
                threadsin.pop(0)


class Guest(Thread):
    def __init__(self, pers):
        super().__init__()
        self.pers = pers

    def run(self): #От формирования потока Гостей до постановки их в очередь
        global thrin, throut, threadsin, threadsout
        # Формирование потока из гостей, которые собираются сходить в кафе
        t_in  = self.pers
        thrin = Thread(target=waiting(a=1, b=5, name=t_in), name=t_in)
        threadsin.append(thrin)

class Cafe():
    def __init__(self, *args):
        self.args = tables

    def guest_arrival(self, *args):
        self.args = args
        #Ожидание гостей
        while threadsin == []:
            sleep(1)
        # Гость пришел
        in_amount = 0
        while in_amount < len(guests_names):
            if threadsin != []:
                thr_0 = threadsin.pop(0)
                pers_in = thr_0.name
                pers_queue_in.put(pers_in)
                print(f'{pers_in} пришёл(-шла) в кафе. ')
                in_amount += 1
                Table.table_for_service(guest=pers_in)


    def discuss_guests(self):
        #Если есть очередь из гостей
        while not pers_queue_in.empty():
            #Ждём, пока освободится стол для посадки гостей
            while threads_table == []:
                sleep(1)
            # Ждём, пока освободится стол для посадки гостей
            while threads_table != []:
            # Стол освободился
                if threads_table != []:
                    # Первый освободившийся стол
                    tab_0 = threads_table[0]
                    # Номер свободного стола
                    table_in = int(tab_0.name)
                    # Если гостей нет, то и обслуживат некого
                    if pers_queue_in.qsize() == 0:
                        break
                    # Берём Гостя из очереди
                    pers_in = pers_queue_in.get()
                    # Достаём свободный стол
                    find_table = [inst for inst in tables if inst.number == table_in]
                    # Освобождаем стол от уже обслуженного гостя
                    pers_out = find_table[0].guest
                    # Усаживаем за свободный стол гостя
                    find_table[0].guest = pers_in
                    print(f'{pers_out} покушал(-а) и ушёл(ушла).')
                    print(f'Стол номер {table_in} свободен.')
                    # Удаляем стол из дальнейшего рассмотрения
                    threads_table.pop(0)
                    # Если есть ещё очередь из гостей - обслуживаем столы
                    if pers_queue_in.qsize() != 0:
                        Table.table_after_service(table=table_in, guest=pers_in)
                    else:
                        cafe.ending()


    def ending(self):
        print(f'            Последний стол освободился. Клиентов больше нет!')



# Создание столов
# tables = [Table(number) for number in range(1, 3)]
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
# guests_names = [
# 'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya']
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name).start() for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(Table)

# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

