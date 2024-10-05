def add_everything_up(a, b):
    try:
        res = a + b
    except TypeError:
        a_str = str(a)
        b_str = str(b)
        res = a_str + b_str
    return res


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
