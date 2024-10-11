
from random import uniform
from threading import Thread, Lock
from time import sleep

lock = Lock()

class Bank():
    balance = 0

    def deposit(self):
        for i_dep in range(100):
            dep_add = int(uniform(50,500))
            lock.acquire()
            if Bank.balance >= 500  and lock.locked():
                lock.release()
                sleep(0.1)
            else:
                Bank.balance = Bank.balance + dep_add
                print(f'Пополнение: {dep_add}. Баланс: {Bank.balance}')
                sleep(0.1)
                lock.release()
        return

    def take (self):
        for i_take in range(100):
            lock.acquire()
            dep_take = int(uniform(50,500))
            print(f'Запрос на {dep_take}')
            if dep_take <= Bank.balance:
                Bank.balance = Bank.balance - dep_take
                print(f'Снятие: {dep_take}. Баланс: {Bank.balance}')
                lock.release()
                sleep(0.1)
            else:
                print((f'Запрос отклонён, недостаточно средств'))
                lock.release()
                sleep(0.1)
        return
bk = Bank()
# Bank.deposit()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')





