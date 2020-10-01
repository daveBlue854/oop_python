from unittest import TestCase

from src.Bin import Bin
from src.Outcome import Outcome


class testBin(TestCase):

    def testBinElements(self):
        outcomes = {Outcome('red', 2), Outcome('blue', 3)}
        b = Bin(outcomes)
        c = Bin(outcomes)
        self.assertEqual(b, frozenset(outcomes))
        self.assertEqual(c, frozenset(outcomes))
