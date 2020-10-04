import unittest
from unittest.mock import MagicMock

from src.Bin import Bin
from src.BinBuilder import BinBuilder
from src.Table import Table
from src.Wheel import Wheel
from src.roulette import Passenger57, Game


class TestGame(unittest.TestCase):

    @classmethod
    def setUp(self) -> None:
        self.w = Wheel()
        binBuilder = BinBuilder(self.w)
        binBuilder.buildBins()
        self.t = Table([])
        self.g = Game(self.t, self.w)

    def test_init(self):
        self.assertTrue(type(self.g) == Game)

    def test_cycle_placeBets(self):
        p1 = Passenger57(self.t, self.w)
        p1.placeBets = MagicMock()
        self.w.next = MagicMock(return_value=self.w.getOutcomeByName('black'))
        p1.isPlaying = MagicMock(return_value=True)

        self.g.cycle(p1)

        p1.placeBets.assert_called()
        self.w.next.assert_called()

    def test_cycle_win_lose(self):
        p1 = Passenger57(self.t, self.w)
        p1.win = MagicMock()
        p1.lose = MagicMock()
        black = self.w.getOutcomeByName('black')
        self.w.next = MagicMock(return_value=Bin([black]))
        p1.isPlaying = MagicMock(return_value=True)

        self.g.cycle(p1)

        p1.win.assert_called()
        p1.lose().assert_not_called()

    def testMockWheel(self):
        self.w.next = MagicMock(return_value=self.w.getOutcomeByName('black'))
        self.assertTrue(self.w.next().name == 'black')

    def testIsPlaying(self):
        p1 = Passenger57(self.t, self.w)
        p1.isPlaying = MagicMock(return_value=False)
        p1.placeBets = MagicMock()
        self.w.next = MagicMock(return_value=self.w.getOutcomeByName('black'))

        self.g.cycle(p1)
        p1.placeBets.assert_not_called()


if __name__ == '__main__':
    unittest.main()
