import unittest
import tests_12_3


RunnerST = unittest.TestSuite()
RunnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
RunnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

run_tour = unittest.TextTestRunner(verbosity=2)
run_tour.run(RunnerST)
