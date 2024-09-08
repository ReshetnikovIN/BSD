def string_info(str_):
    global calls
    str_low = str_.lower()
    str_upp = str_.upper()
    str_len = len(str_)
    tuple_01 = (str_len,) + (str_upp,) + (str_low,)
    calls +=1
    return tuple_01


def is_contains(str_in, list_to_search):
    global calls
    str_low = str_in.lower()
    TF = False
    for id in list_to_search:
        lst_low = id.lower()
        if lst_low == str_low:
            TF = True
    calls += 1
    return TF



calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



