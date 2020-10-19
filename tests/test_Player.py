import unittest

from src.Bet import Bet
from src.BinBuilder import BinBuilder
from src.Player import Player
from src.Table import Table
from src.Wheel import Wheel


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        self.w = Wheel()
        bb = BinBuilder(self.w)
        bb.buildBins()
        self.t = Table()
        self.p = Player(self.t, self.w)

    def test_default_budget(self):
        self.assertEqual(self.p.budget, self.p.BUDGET_MIN_DEFAULT_MULTIPLIER * self.t.minimum)

    def test_default_duration(self):
        self.assertEqual(self.p.duration, self.p.DURATIONS_MIN_DEFAULT)

    def test_win(self):
        budgetBefore = self.p.budget
        outcome = self.w.getOutcomeByName("0")
        bet = Bet(self.t.minimum, outcome)
        self.p.win(bet)
        self.assertEqual(self.p.budget, budgetBefore + bet.amount * (outcome.odds + 1))

    def test_placeBets_BudgetReduction(self):
        budgetBefore = self.p.budget
        self.p.placeBets()
        self.assertEqual(budgetBefore, self.p.budget + self.t.minimum)

    def test_placeBets_DurationReduction(self):
        durationBefore = self.p.duration
        self.p.placeBets()
        self.assertEqual(durationBefore, self.p.duration + 1)

    def test_isPlaying_trueWhenDurationAndBudgetpositive(self):
        self.assertTrue(self.p.isPlaying())

    def test_isPlaying_falseWhenDurationAndBudgetNegative(self):
        self.p.budget = 0
        self.assertFalse(self.p.isPlaying())
        self.p.budget = 100
        self.p.duration = 0
        self.assertFalse(self.p.isPlaying())

        if __name__ == '__main__':
            unittest.main()
