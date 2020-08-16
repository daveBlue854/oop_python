from unittest import TestCase
from src.roulette import Table, Bet, Outcome, BetOdds, TABLE_LIMIT, TABLE_MINIMUM, InvalidBet

outcome = Outcome('red', BetOdds.EVEN_MONEY)


class testTable(TestCase):
    def testTableInit(self):
        betList = [Bet(30, outcome), Bet(10, outcome)]
        t = Table(betList)
        self.assertCountEqual(t.bets, betList)

    def testPlaceBet(self):
        ilegalBet = Bet(TABLE_LIMIT + 1, outcome)
        t = Table()
        with self.assertRaises(InvalidBet):
            t.placeBet(ilegalBet)

    def testIsValidOverLimit(self):
        betList = [Bet(TABLE_LIMIT + 1, outcome)]
        t = Table(betList)
        with self.assertRaises(InvalidBet):
            t.isValid()

    def testIsValidUnderMinimum(self):
        betList = [Bet(TABLE_MINIMUM - 0.1, outcome)]
        t = Table(betList)
        with self.assertRaises(InvalidBet):
            t.isValid()

    def testIter(self):
        betList = [Bet(30, outcome), Bet(10, outcome), Bet(5, outcome)]
        t = Table(betList)
        for i, el in enumerate(t):
            self.assertEqual(betList[i], el)

    def testStr(self):
        betList = [Bet(30, outcome)]
        t = Table(betList)
        self.assertEqual(str(t), "Bets list: ['Outcome: red, odds are 1, amount: 30']")
