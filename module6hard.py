import math


class Figure():
    sides_count = 0
    __sides = []
    color = (255, 255, 255)
    filled = True

    def __init__(self, color, *args, sides_count = 0, filled = True):
        self.__sides  = args
        self.__color = color
        self.filled = True

        sides_count = 0
        for i_side in self.__sides:
             sides_count += 1

    def get_color(self):
        return self.__color

    def __is_valid_color(self, color_test):
        color_res = True
        color_sum = 0

        for ind_color in color_test:
            if 0 <= ind_color <= 255:
                pass
            else:
                color_sum += 1
        if color_sum > 0:
            color_res = False

        return color_res

    def set_color(self, r, g, b):
        color_change = ()
        color = color_change
        color_change = color_change + (r,) + (g,) + (b,)

        if self.__is_valid_color(color_change):
            self.__color = color_change
        return color

    def __is_valid_sides(self, *args):
        valid_res = False
        find_class = issubclass(self.__class__, Cube)
        bool_amount = 0
        if len(args) == len(self.__sides):
            for i_side in range(self.sides_count):
                for i_curr_side in self.__sides:
                    if isinstance(i_side, int) and i_side > 0:
                        bool_amount += 1
            if bool_amount == len(args):
                valid_res = True
        else:
            if issubclass(self.__class__, Cube):
                self.__sides = list(self.__sides)
                for ind in range(self.sides_count - 1):
                    self.__sides.append(self.__sides[0])

                valid_res = False

    def get_sides(self):
        return self.__sides

    def __len__ (self):
        len_amount = 0
        for i_curr_side in self.__sides:
            len_amount +=i_curr_side
        return len_amount

    def set_sides(self, *new_sides):
        ind = 0
        if self.sides_count == len(new_sides):
            self.__sides = list(self.__sides)
            self.__sides[0] = new_sides[0]
        else:
            if issubclass(self.__class__, Cube):
                self.__sides = list(self.__sides)
                for ind_cub in range(self.sides_count - 1):
                    self.__sides.append(self.__sides[0])

class Circle(Figure):
    sides_count = 1
    __radius = 0
    filled = True

    def __init__(self, color, *args, sides_count = 12, filled = True):
        super().__init__(color, *args)
        self.__sides = args

    def get_square(self):
        Circle_sq = math.pi * __radius ** 2
        return Circle_sq

class Triangle(Figure):
    sides_count = 3
    __sides = []
    filled = True

    def __init__(self, color, *args, sides_count = 3, filled = True):
        super().__init__(color, *args)
        self.__sides = args

    if len(__sides) != sides_count:
        for ind_tri in __sides:
            __sides[ind_tri] = 1

    def get_square(self, __sides):
        pol_per = 0
        for side in __sides:
            pol_per += side / 2
        tri_sq = math.sqrt(pol_per * (pol_per - side[0]) * (pol_per - side[1]) * (pol_per - side[2]))
        return tri_sq

class Cube(Figure):
    sides_count = 12
    filled = True
    __sides = []

    def __init__(self, color, *args, sides_count = 12, filled = True):
        super().__init__(color, *args)
        self.__sides = args
        if len(args) == 1:
            ind_cub = 0
            for ind_cub in range(self.sides_count):
                self.__sides = list(self.__sides)
                self.__sides.append(args[0])
        else:
            self.__sides = args
        Figure.__sides = self.__sides

    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
