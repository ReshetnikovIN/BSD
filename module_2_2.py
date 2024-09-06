first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second and second == third:
    print('3')
elif first == second or second == third:
    print('2')
else:
    print('0')

