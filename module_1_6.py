my_dict = {'Igor': 1962, 'Toma': 1962, 'Roma': 1987, 'Masha': 1993}
print('Работа со словарями')
print (my_dict)
print (my_dict['Toma'])
print (my_dict.get('Sveta', 'Нет такого имени "Sveta"'))
my_dict.update({'Natasha': 1989, 'Ivan': 1995})
print (my_dict)
deliting = my_dict.pop('Igor')
print(deliting)
print (my_dict)

print('Работа с множествами')
my_set = {'Igor', 1962, 'Toma', 1962, 'Roma', 1987, 'Masha', 1993, False, False, True}
print (my_set)
adding = {'Natasha', 1989, 'Ivan', 1995}
my_set = my_set | adding
print(my_set)
my_set.discard('Igor')
print(my_set)
