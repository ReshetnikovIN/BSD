from pyexpat import ExpatError


class IncorrectVinNumber (Exception):
    def __init__(self, message, vin_number):
        self.message = message
        self.vin_number = vin_number

class IncorrectCarNumbers (Exception):
    def __init__(self, message, numbers):
        self.message = message
        self.numbers = numbers

class Car():
    def __init__(self, model: str, vin, numbers: str):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):
        valid_res = True
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber ('Некорректный тип vin номер', vin_number)
            valid_res = False

        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера', vin_number)
            valid_res = False
        return valid_res

    def __is_valid_numbers(self, numbers):
        valid_res = True
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers ('Некорректный тип данных для номеров', numbers)
            valid_res = False
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера', numbers)
            valid_res = False
        return valid_res

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
