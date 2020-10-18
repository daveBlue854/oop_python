from unittest import TestCase
from src.Bet import Bet
from src.roulette import *


class TestPassenger57(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.w = Wheel()
        binBuilder = BinBuilder(cls.w)
        binBuilder.buildBins()
        cls.t = Table()
        cls.p57 = Passenger57(cls.t, cls.w)

    def testInit(self):
        self.assertEqual(self.p57.table, self.t)
        self.assertEqual(self.p57.black, self.w.getOutcomeByName('black'))

    def testPlaceBets(self):
        self.p57.placeBets()
        self.assertEqual(len(self.t.bets), 1)
        placedBet: Bet = self.t.bets[0]
        self.assertEqual(placedBet.__str__(), Bet(10, self.w.getOutcomeByName('black')).__str__())
