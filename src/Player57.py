from src.Bet import Bet
from src.Player import Player
from src.Table import Table
from src.Wheel import Wheel


class Passenger57(Player):
    BLACK_OUTCOME_NAME = 'black'

    def __init__(self, table: Table, wheel: Wheel) -> None:
        super().__init__(table, wheel)
        self.black = wheel.getOutcomeByName(Passenger57.BLACK_OUTCOME_NAME)

    def playBySpecificStrategy(self) -> None:
        blackBet = Bet(10, self.black)
        self.table.placeBet(blackBet)
