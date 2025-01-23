import unittest
from pprint import pprint

from runner_and_tournament import Runner
from runner_and_tournament import Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        # print(f'test_walk')
        some_walk = Runner('some_walk')
        for _ in range(10):
            some_walk.walk()
        self.assertEqual(some_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        # print(f'test_run')
        some_run = Runner('some_run')
        for _ in range(10):
            some_run.run()
        self.assertEqual(some_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        # print(f'test_challenge')
        some_challenge_run = Runner('some_challenge_run')
        some_challenge_walk = Runner('some_challenge_walk')
        for _ in range(10):
            some_challenge_run.run()
            some_challenge_walk.run()
        self.assertEqual(some_challenge_run.distance, some_challenge_walk.distance)
        # self.assertEqual('Ник', 'Ник')


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
       self.all_results = {}

    def setUp(self):
        # print(f'Загрузка бегунов')
        self.usain = Runner('Усейн', 10)
        self.andr = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    is_frozen = True
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        new_tour_1 = Tournament(90, self.usain, self.nik)
        res = new_tour_1.start()
        els = res[list(res.keys())[-1]]
        self.all_results[1] = res
        self.assertTrue(els == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        new_tour = Tournament(90, self.andr, self.nik)
        res = new_tour.start()
        els = res[list(res.keys())[-1]]
        self.all_results[2] = res
        self.assertTrue(els == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        new_tour = Tournament(90, self.usain, self.andr, self.nik)
        res = new_tour.start()
        els = res[list(res.keys())[-1]]
        self.all_results[3] = res
        self.assertTrue(els == 'Ник')

    @classmethod
    def tearDownClass(self):
        print(f'Результаты')
        pprint(self.all_results)




if __name__ == "__main__":
    unittest.main

