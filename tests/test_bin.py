from unittest import TestCase
from src.roulette import Outcome
from src.roulette import Bin


class testBin(TestCase):
    def testBinElements(self):
        outcomes = {Outcome('red', 2), Outcome('blue', 3)}
        b = Bin(outcomes)
        c = Bin(outcomes)
        self.assertEqual(b, frozenset(outcomes))
        self.assertEqual(c, frozenset(outcomes))
