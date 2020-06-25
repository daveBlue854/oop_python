from dataclasses import dataclass


@dataclass(frozen=True)
class Outcome:
    name: str
    odds: int

    def winAmount(self, amount: int):
        return self.odds * amount


class Bin(frozenset):
    pass
