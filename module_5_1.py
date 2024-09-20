class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(House, new_floor):
        new_floor = int(new_floor)
        # print(new_floor)
        if new_floor > House.number_of_floors:
            print('Такого этажа не существует')
        else:
            for ind in range(1, new_floor+1):
                print(ind)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


