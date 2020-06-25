from unittest import TestCase
from src import roulette


class TestOutcome(TestCase):
    def testStr(self):
        o = roulette.Outcome('red', 1)
        self.assertEqual(str(o), "red, 1")

    def testRepr(self):
        o = roulette.Outcome('red', 1)
        self.assertEqual(repr(o), "Outcome : name='red', odds=1")

    def testEquality(self):
        o1 = roulette.Outcome('red', 1)
        o2 = roulette.Outcome('red', 1)
        self.assertEqual(o1, o2)

    def testInEquality(self):
        o1 = roulette.Outcome('blue', 1)
        o2 = roulette.Outcome('red', 1)
        self.assertNotEqual(o1, o2)

    def testHash(self):
        o1 = roulette.Outcome('red', 1)
        o2 = roulette.Outcome('red', 1)
        self.assertEqual(hash(o1), hash(o2))

    def testWinAmount(self):
        o1 = roulette.Outcome('red', 2)
        self.assertEqual(o1.winAmount(3), 6)
