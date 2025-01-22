import unittest
from pprint import pprint

from runner_and_tournament import Runner
from runner_and_tournament import Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
       self.all_results = {}

    def setUp(self):
        # print(f'Загрузка бегунов')
        self.usain = Runner('Усейн', 10)
        self.andr = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    def test_1(self):
        new_tour_1 = Tournament(90, self.usain, self.nik)
        res = new_tour_1.start()
        els = res[list(res.keys())[-1]]
        self.all_results[1] = res
        self.assertTrue(els == 'Ник')

    def test_run_2(self):
        new_tour = Tournament(90, self.andr, self.nik)
        res = new_tour.start()
        els = res[list(res.keys())[-1]]
        self.all_results[2] = res
        self.assertTrue(els == 'Ник')

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


    # def test_challenge(self):
    #     some_challenge_run = Runner('some_challenge_run')
    #     some_challenge_walk = Runner('some_challenge_walk')
    #     for _ in range(10):
    #         some_challenge_run.run()
    #         some_challenge_walk.run()
    #     self.assertEqual(some_challenge_run.distance, some_challenge_walk.distance)


if __name__ == "__main__":
    unittest.main
    # usain = Runner('Усейн', 10)
    # andr = Runner('Андрей', 9)
    # nik = Runner('Ник', 3)
    # new_tour = Tournament(90, (usain, nik))
    # tour_res = new_tour.start()
    # print(f'new_tour - {tour_res}')
