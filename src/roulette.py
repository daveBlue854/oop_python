import os
from dataclasses import dataclass
import random


@dataclass(frozen=True)
class Outcome:
    name: str
    odds: int

    def winAmount(self, amount: int):
        return self.odds * amount


class Bin(set):
    """
    whats going on?
     I thought this should extend 'frozenset'
    but then I could not implement addOutcome
    method on Wheel.
    not sure if i did something wrong but for now lets roll
    """
    pass


class Wheel():
    def __init__(self):
        self.bins = tuple(Bin() for i in range(38))
        self.rng = random.Random()

    def get(self, number: int):
        return self.bins[number]

    def addOutcome(self, number: int, outcome: Outcome):
        self.bins[number].add(outcome)

    def next(self):
        randIndex = self.rng.randint(0, 37)
        return self.bins[randIndex]
