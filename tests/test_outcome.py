from unittest import TestCase
from src.roulette import Outcome


class TestOutcome(TestCase):

    def testFields(self):
        o = Outcome('red', 1)
        self.assertEqual(o.name, 'red')
        self.assertEqual(o.odds, 1)

    def testStr(self):
        o = Outcome('red', 1)
        self.assertEqual(str(o), "Outcome(name='red', odds=1)")

    def testRepr(self):
        o = Outcome('red', 1)
        self.assertEqual(repr(o), "Outcome(name='red', odds=1)")

    def testEquality(self):
        o1 = Outcome('red', 1)
        o2 = Outcome('red', 1)
        self.assertEqual(o1, o2)

    def testInEquality(self):
        o1 = Outcome('blue', 1)
        o2 = Outcome('red', 1)
        self.assertNotEqual(o1, o2)

    def testHash(self):
        o1 = Outcome('red', 1)
        o2 = Outcome('red', 1)
        self.assertEqual(hash(o1), hash(o2))

    def testWinAmount(self):
        o1 = Outcome('red', 2)
        self.assertEqual(o1.winAmount(3), 6)

