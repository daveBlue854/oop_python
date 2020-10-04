from src.Bet import Bet
from src.Table import Table
from src.Wheel import Wheel


class Player():
    def __init__(self, table: Table, wheel: Wheel):
        self.table = table
        self.wheel = wheel

    def isPlaying(self):
        pass

    def placeBets(self):
        pass

    def win(self, bet: Bet):
        pass

    def lose(self, bet: Bet):
        pass
