from unittest import TestCase
from src import roulette


class TestOutcome(TestCase):
    def testOutcome(self):
        o = roulette.Outcome('red', 1)
        self.assertEqual(str(o), "blue  ,1")
