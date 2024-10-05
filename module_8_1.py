def add_everything_up(a, b):
    try:
        res = a + b
    except:
        a_type = type(a)
        b_type = type(b)
        print(f'Переменные разных типов. а = {a} - имеет тип {a_type}, b = {b} имеет тип {b_type}.')
    else:
        a_type = type(a)
        print(f'Переменные одинаковых типов  -  {a_type}.')
    finally:
        a_str = str(a)
        b_str = str(b)
        res = a_str + b_str
    return res


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
