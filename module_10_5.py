import os
import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    file = open(name, 'r')
    while True:
        string = file.readline()
        if not string:
            break
        all_data.append(string)
    file.close()

files = []
if __name__ == '__main__':
    files = [os.path.join(os.getcwd(), r'Files\file ' + str(i + 1) + '.txt') for i in range(1, 4)]
    # Линейный вызов
    start_time = datetime.now()
    files = []
    for i in range(4):
        start_time_ = datetime.now()
        my_cwd = os.getcwd()
        name = r'Files\file ' + str(i + 1) + '.txt'
        path_name = os.path.join(my_cwd, name)
        read_info(path_name)
        end_time_ = datetime.now()
        print(f'Program time for file {str(i + 1)}.txt- {end_time_ - start_time_}')
    end_time = datetime.now()
    print(f'Program time for all files line method - {end_time - start_time}\n')

    # Многопроцессный
    start_time_mp = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        # print(files)
        pool.map(read_info, files)
    end_time_mp = datetime.now()
    print(f'Program time for all files with multiprocessing (4)- {end_time_mp - start_time_mp}')

# Program time for file 1.txt- 0:00:01.575436
# Program time for file 2.txt- 0:00:01.565026
# Program time for file 3.txt- 0:00:01.548541
# Program time for file 4.txt- 0:00:00.151617
# Program time for all files line method - 0:00:04.840620
#
# Program time for all files with multiprocessing (4)- 0:00:00.033907
