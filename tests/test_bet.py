from unittest import TestCase

from src.Bet import Bet
from src.Outcome import Outcome


class TestBet(TestCase):

    def testInit(self):
        o = Outcome('red', 1)
        b = Bet(30, o)
        self.assertEqual(type(b), type(Bet(30, o)))

    def testWinAmount(self):
        o = Outcome('red', 1)
        b = Bet(1, o)
        self.assertEqual(b.winAmont(), 2)

    def testLoseAmount(self):
        o = Outcome('red', 1)
        b = Bet(1, o)
        self.assertEqual(b.loseAmount(), 1)
