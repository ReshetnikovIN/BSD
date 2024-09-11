def get_multiplied_digits(number):
    str_number = str(number)
    str_number_0 = str_number.replace('0', '')
    first = int(str_number_0[0])
    str_len = len(str_number_0)
    if str_len <= 1:
        return (str_number_0)
    else:
        m =  get_multiplied_digits((str_number_0[1:]))
        return (int(m) * first)


result = get_multiplied_digits(40203)
print(result)

