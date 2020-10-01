from src.Outcome import Outcome


class Bet:
    """
    The collected notion of a:
    (1)Player, placing an
    (2)amount on an
    (3)Outcome
    """

    def __init__(self, amount: int, outcome: Outcome):
        self.amount = amount
        self.outcome = outcome

    def winAmont(self):
        return self.amount + self.outcome.winAmount(self.amount)

    def loseAmount(self):
        return self.amount

    def __str__(self):
        return f'Outcome: {self.outcome}, amount: {self.amount}'


class InvalidBet(Exception):
    pass
