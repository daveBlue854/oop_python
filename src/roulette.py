from dataclasses import dataclass

from src.Bet import Bet
from src.BinBuilder import BinBuilder
from src.Table import Table
from src.Wheel import Wheel


class Passenger57:
    BLACK_OUTCOME_NAME = 'black'

    def __init__(self, table: Table, wheel: Wheel) -> None:
        self.table = table
        self.black = wheel.getOutcomeByName(Passenger57.BLACK_OUTCOME_NAME)

    def placeBets(self) -> None:
        blackBet = Bet(10, self.black)
        self.table.placeBet(blackBet)

    def win(self, bet: Bet) -> None:
        moneyWon = bet.winAmont()
        print(f'we have won {moneyWon}')

    def lose(self, bet: Bet) -> None:
        moneyLost = bet.loseAmount()
        print(f'we have lost {moneyLost}')


@dataclass()
class Game():
    wheel: Wheel
    table: Table

    def cycle(self, player: Passenger57):
        player.placeBets()
        binTheWheelGot = self.wheel.next()
        for bet in self.table:
            if bet.outcome in binTheWheelGot:
                player.win(bet)
            else:
                player.lose(bet)
        self.table.bets = []


class Demo():
    def __init__(self):
        pass

    def run(self):
        w = Wheel()
        binBuilder = BinBuilder(w)
        binBuilder.buildBins()
        t = Table([])
        g = Game(w, t)
        p1 = Passenger57(t, w)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)


d = Demo()
d.run()
