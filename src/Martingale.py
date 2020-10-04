from src.Bet import Bet
from src.Player import Player
from src.Table import Table
from src.Wheel import Wheel


class Martingale(Player):
    BLACK_OUTCOME_NAME = 'black'

    def __init__(self, table: Table, wheel: Wheel):
        super().__init__(table, wheel)
        self.lossCount = 0
        self.stake = 1000

    def placeBets(self):
        blackOutcome = self.wheel.getOutcomeByName(Martingale.BLACK_OUTCOME_NAME)
        amount = 10 * (2 ** self.lossCount)
        currentBet = Bet(amount, blackOutcome)
        self.table.placeBet(currentBet)
        self.stake -= amount

    def lose(self, bet: Bet):
        self.lossCount += 1

    def win(self, bet: Bet):
        self.stake += bet.winAmont()
        self.lossCount = 0
