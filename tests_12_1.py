import unittest
from runner import Runner

# class RunnerTest():
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        some_walk = Runner('some_walk')
        for _ in range(10):
            some_walk.walk()
        self.assertEqual(some_walk.distance, 50)
    def test_run(self):
        some_run = Runner('some_run')
        for _ in range(10):
            some_run.run()
        self.assertEqual(some_run.distance, 100)

    def test_challenge(self):
        some_challenge_run = Runner('some_challenge_run')
        some_challenge_walk = Runner('some_challenge_walk')
        for _ in range(10):
            some_challenge_run.run()
            some_challenge_walk.run()
        self.assertEqual(some_challenge_run.distance, some_challenge_walk.distance)


if __name__ == "__main__":
    unittest.main

