import unittest
from unittest.mock import MagicMock

from src.Bet import Bet
from src.Bin import Bin
from src.BinBuilder import BinBuilder
from src.Martingale import Martingale
from src.Table import Table
from src.Wheel import Wheel
from src.roulette import Game


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.t = Table([])
        self.w = Wheel()
        binBuilder = BinBuilder(self.w)
        binBuilder.buildBins()
        self.blackOutcome = self.w.getOutcomeByName('black')
        self.redOutcome = self.w.getOutcomeByName('red')
        self.blackOutcomeBin = Bin([self.blackOutcome])
        self.redOutcomeBin = Bin([self.redOutcome])
        self.m = Martingale(self.t, self.w)
        self.m.isPlaying = MagicMock(return_value=True)
        self.g = Game(self.t, self.w)

    def testLossCount(self):
        self.assertEqual(self.m.lossCount, 0)
        self.m.lose(Bet(1, self.blackOutcome))
        self.assertEqual(self.m.lossCount, 1)

    def testWinLossCountInit(self):
        myBet = Bet(1, self.blackOutcome)
        self.m.lose(myBet)
        self.m.win(myBet)
        self.assertEqual(self.m.lossCount, 0)

    def testStakeOnLoseAndWin(self):
        self.assertEqual(self.m.stake, 1000)
        myBet = Bet(10, self.blackOutcome)
        self.m.placeBets()
        self.m.lose(myBet)
        self.assertEqual(self.m.stake, 990)
        self.m.placeBets()
        self.m.win(myBet)
        self.assertEqual(self.m.stake, 990)
        self.m.placeBets()
        self.m.win(myBet)
        self.assertEqual(self.m.stake, 1000)

    def test_placeBets(self):
        wheelSpins = [self.redOutcomeBin, self.redOutcomeBin, self.redOutcomeBin, self.blackOutcomeBin,
                      self.blackOutcomeBin]
        correctLossCount = [0, 1, 2, 3, 0]
        zipped = zip(wheelSpins, correctLossCount)
        for z in zipped:
            self.assertEqual(self.m.lossCount, z[1])
            self.w.next = MagicMock(return_value=z[0])
            self.g.cycle(self.m)


if __name__ == '__main__':
    unittest.main()
