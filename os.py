import os

# print('Текущая директория: ', os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')
# print('Текущая директория: ', os.getcwd())
# os.makedirs('thurd\\fourth')
# print(os.listdir())
# for i in os.walk('.'):
#     print(i)
os.chdir(r'C:\Users\Игорь\PycharmProjects\pythonProject1')
print('Текущая директория: ', os.getcwd())
# print(os.listdir())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(dirs)
# print(file)
# os.startfile('test.txt')
# print(os.stat('test.txt').st_size)
os.system('pip install random2')
