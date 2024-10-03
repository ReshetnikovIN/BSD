import io
from pprint import pprint

def custom_write(file_name: str, strings: list):
    strings_positions = {}
    string_in = ''
    file = open(file_name, 'w', encoding='utf-8')
    count = 1
    tupl_out = ()
    for ind in strings:
        ind_b = file.tell()
        tupl_in = ()
        tupl_in = tupl_in + (count,) + (ind_b,)
        strings_positions[tupl_in] = ind
        string_in = str(ind) + '\n'
        file_in = file.write(string_in)
        count += 1
    file.close()

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
