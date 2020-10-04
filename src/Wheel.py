import random

from src.Bin import Bin
from src.Outcome import Outcome


class Wheel:
    def __init__(self):
        self.bins = tuple(Bin() for _ in range(38))
        self.rng = random.Random()
        self.allOutcomes = dict()

    def getOutcomeByIndex(self, number: int) -> Outcome:
        return self.bins[number]

    def getOutcomeByName(self, name: str) -> Outcome:
        return self.allOutcomes[name]

    def addOutcome(self, number: int, outcome: Outcome) -> None:
        self.allOutcomes[outcome.name] = outcome
        self.bins[number].add(outcome)

    def next(self) -> Bin:
        randIndex = self.rng.randint(0, 37)
        return self.bins[randIndex]
