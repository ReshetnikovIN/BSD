import os
import time

directory = os.getcwd()
# print(directory)
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.getcwd()
        filetime = os.stat(file).st_ctime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(file).st_size
        parent_dir = os.path.dirname(directory)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:{formatted_time}, Родительская директория: {parent_dir}')