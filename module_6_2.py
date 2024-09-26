class Vehicle():
    owner: str
    __model: str
    __engine_power: int
    __color: str
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(__model):
        print('Модель: ', __model)

    def get_horsepower (__engine_power):
        print(f'Мощность двигателя: {__engine_power}')

    def get_color (__color):
        print(f'Цвет: {__color}')

    def print_info(self):
        Vehicle.get_model(self.__model)
        Vehicle.get_horsepower(self.__engine_power)
        Vehicle.get_color(self.__color)
        print(f'Владелец: {self.owner}')

    def set_color (self, new_color):
        change = False
        new_color: str
        for i_col in Vehicle.__COLOR_VARIANTS:
            if i_col.lower() == new_color.lower():
                self.__color = new_color
                change = True
        if not change:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan (Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()









class Sedan(Vehicle):
    pass
