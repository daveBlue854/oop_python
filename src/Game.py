from dataclasses import dataclass

from src.Player import Player
from src.Table import Table
from src.Wheel import Wheel


@dataclass()
class Game():
    table: Table
    wheel: Wheel

    def cycle(self, player: Player):
        if not player.isPlaying():
            return
        player.placeBets()
        binTheWheelGot = self.wheel.next()
        for bet in self.table:
            if bet.outcome in binTheWheelGot:
                player.win(bet)
            else:
                player.lose(bet)
        self.table.bets = []
