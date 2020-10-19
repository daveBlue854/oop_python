from src.Bet import Bet
from src.Table import Table
from src.Wheel import Wheel


class Player():
    BUDGET_MIN_DEFAULT_MULTIPLIER = 100
    DURATIONS_MIN_DEFAULT = 250

    def __init__(self, table: Table, wheel: Wheel):
        self.table = table
        self.wheel = wheel
        self.budget = self.BUDGET_MIN_DEFAULT_MULTIPLIER * self.table.minimum
        self.duration = self.DURATIONS_MIN_DEFAULT

    def isPlaying(self):
        return self.duration > 0 and self.budget > 0

    def placeBets(self):
        self.budget -= self.table.minimum
        self.duration -= 1
        self.playBySpecificStrategy()

    def win(self, bet: Bet):
        self.budget += bet.winAmont()

    def lose(self, bet: Bet):
        self.budget -= bet.loseAmount()

    def playBySpecificStrategy(self):
        pass
