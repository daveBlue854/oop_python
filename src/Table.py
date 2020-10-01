from functools import reduce
from typing import List

from src.Bet import Bet, InvalidBet

TABLE_LIMIT = 300
TABLE_MINIMUM = 5


class Table:
    limit = TABLE_LIMIT
    minimum = TABLE_MINIMUM

    def __init__(self, bets: List[Bet] = []):
        self.bets = bets

    def placeBet(self, bet: Bet):
        self.bets.append(bet)
        try:
            self.isValid()
        except InvalidBet as e:
            self.bets.remove(bet)
            raise e

    def isValid(self):
        tabelBetsSum = reduce(lambda sum, b: sum + b.amount, self.bets, 0)
        if tabelBetsSum > TABLE_LIMIT:
            raise InvalidBet(f'Table Bets is {tabelBetsSum} which is higher than table limit which is {TABLE_LIMIT}')
        elif tabelBetsSum < TABLE_MINIMUM:
            raise InvalidBet(f'Table Bets is {tabelBetsSum} which is lower than table minimum which is {TABLE_MINIMUM}')

    def __iter__(self):
        return self.bets.__iter__()

    def __str__(self):
        s = 'Bets list: '
        betsList = [str(bet) for bet in self.bets]
        return s + str(betsList)
