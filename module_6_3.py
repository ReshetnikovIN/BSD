
class Horse():
    x_distance = 0
    sound = 'Frrr'
    def __init__(self):
        super().__init__()

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance

class Eagle():
    y_distance = 0
    sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance

class Pegasus (Eagle, Horse):
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):
        hr = Horse.run(self, dx)
        ef = Eagle.fly(self, dy)

    def get_pos(self):
        peg_tupl = ()
        peg_tupl = peg_tupl + (self.x_distance,) + (self.y_distance,)
        return peg_tupl

    def voice(self):
        print(self.sound)



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()







