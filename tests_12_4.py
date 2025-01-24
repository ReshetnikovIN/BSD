import logging
import unittest

from rt_with_exceptions import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        some_walk = Runner('Nik', speed= -7)
        for _ in range(10):
            some_walk.walk()
        self.assertEqual(some_walk.distance, 50)

    def test_run(self):
        some_run = Runner(2, speed= 7)
        for _ in range(10):
            some_run.run()
        self.assertEqual(some_run.distance, 100)




logging.basicConfig(level=logging.INFO, filename='runner_tests.log',
                    encoding = "UTF-8", filemode='w', format="%(asctime)s %(levelname)s %(message)s")
logging.debug('Debug mess')
logging.info('Info mess')
logging.warning('Warning mess')
logging.error('Error mess')
logging.critical('Critical mess')





