def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)



print_params(a = 3)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [11, '1+1', True]
values_dict = {'a': 11, 'b': 'STRING', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['23', 23]
print_params(*values_list_2, 42)