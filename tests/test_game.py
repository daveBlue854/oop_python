import unittest
from unittest.mock import MagicMock
from src.roulette import Game, Wheel, Table, Passenger57, BinBuilder, Bin


class TestGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.w = Wheel()
        binBuilder = BinBuilder(cls.w)
        binBuilder.buildBins()
        cls.t = Table([])
        cls.g = Game(cls.w, cls.t)

    def test_init(self):
        self.assertTrue(type(self.g) == Game)

    def test_cycle_placeBets(self):
        p1 = Passenger57(self.t, self.w)
        p1.placeBets = MagicMock()
        self.w.next = MagicMock(return_value=self.w.getOutcomeByName('black'))

        self.g.cycle(p1)

        p1.placeBets.assert_called()
        self.w.next.assert_called()

    def test_cycle_win_lose(self):
        p1 = Passenger57(self.t, self.w)
        p1.win = MagicMock()
        p1.lose = MagicMock()
        black = self.w.getOutcomeByName('black')
        self.w.next = MagicMock(return_value=Bin([black]))

        self.g.cycle(p1)

        p1.win.assert_called()
        p1.lose().assert_not_called()

    def testMockWheel(self):
        self.w.next = MagicMock(return_value=self.w.getOutcomeByName('black'))
        self.assertTrue(self.w.next().name == 'black')


if __name__ == '__main__':
    unittest.main()
