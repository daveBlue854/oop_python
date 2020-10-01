from unittest import TestCase

from src.Bet import InvalidBet


def brokenFunction():
    raise InvalidBet('this is broken')


class testInvalidBet(TestCase):
    def testInvalidBet(self):
        self.assertRaises(InvalidBet, brokenFunction)
