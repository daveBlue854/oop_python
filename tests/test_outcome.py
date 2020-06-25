from unittest import TestCase
from src import roulette


class TestOutcome(TestCase):
    def testStr(self):
        o = roulette.Outcome('red', 1)
        self.assertEqual(str(o), "red, 1")

    def testRepr(self):
        o = roulette.Outcome('red', 1)
        self.assertEqual(repr(o), "Outcome : name='red', odds=1")
