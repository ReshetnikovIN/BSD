class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        for participant in self.participants:
            participant.distance = 0
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers

usain = Runner('Усэйн', 10)
andr = Runner('Андрей', 9)
nik = Runner('Ник', 3)
#
tour_1 = Tournament(90, usain, nik)
# tour_2 = Tournament(90, andr, nik)
# tour_3 = Tournament(90, usain, andr, nik)
#
res_1 = tour_1.start()
# res_2 = tour_2.start()
# res_3 = tour_3.start()
#
els = res_1[list(res_1.keys())[-1]]
# print(f'res_1 - {els} {type(els)}')
# print(f'res_2 - {res_2}')
# print(f'res_3 - {res_3}')
# nik = Runner('Ник', 3)
# print(f'self.nik.name - {nik.name} {type(nik.name)}')
