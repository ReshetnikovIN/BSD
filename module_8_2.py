def personal_sum(numbers):
    result_out = ()
    result  = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result  += number
        except:
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
            incorrect_data += 1
    result_out = result_out + (result,) + (incorrect_data,)
    return result_out

def calculate_average(numbers):
    res_ave = 0
    try:
        res_cort = personal_sum(numbers)
        res_ave = res_cort[0] / (len(numbers) - res_cort[1])
    except ZeroDivisionError:
        res_ave = 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        res_ave = None

    return res_ave

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
