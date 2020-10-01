from dataclasses import dataclass
from src.BetOdds import BetOdds


@dataclass(frozen=True)
class Outcome:
    name: str
    odds: BetOdds

    def winAmount(self, amount: int) -> int:
        return self.odds * amount

    def __str__(self):
        return f'{self.name}, odds are {self.odds}'
