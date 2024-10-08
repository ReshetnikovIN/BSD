import os
from random import choice


first = 'Мама мыла раму'
second = 'Рамена мало было'

out = list(map(lambda first, second: list(first) == list(second), first, second))

print(out)

# ++++++++++++++++++++++++++++++++++++


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        text_for_writing = ''
        file = open(file_name, 'a', encoding='utf-8')
        for data_s in data_set:
            text_for_writing = text_for_writing + str(data_s) + '\n'
        file.write(text_for_writing)
        file.close()

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# +++++++++++++++++++++++++++++++++

class MysticBall():
    def __init__(self, *args):
        self.args = args

    def __call__(self):
        elem = choice(self.args)
        return elem

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
