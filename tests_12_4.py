import logging
import unittest

from rt_with_exceptions import Runner

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            some_walk = Runner('Nik', speed= -7)
            for _ in range(10):
                some_walk.walk()
            self.assertEqual(some_walk.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            some_run = Runner(2, speed= 8)
            for _ in range(10):
                some_run.run()
            self.assertEqual(some_run.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)




logging.basicConfig(level=logging.DEBUG, filename='runner_tests.log',
                    encoding = "UTF-8", filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")
logging.debug('Debug mess')
logging.info('Info mess')
logging.warning('Warning mess')
logging.error('Error mess')
logging.critical('Critical mess')
logging.error("Неожиданная ошибка!", exc_info=True)





