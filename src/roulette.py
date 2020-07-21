from dataclasses import dataclass
import random
from enum import Enum


class BetOdds(Enum):
    STRAIGHT_BET = 35
    SPLIT_BET = 17


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


class BinBuilder():
    def __init__(self, wheel: Wheel):
        self.wheel = wheel

    def generateStraightBets(self):
        for i in range(37):
            outcome = Outcome(f"{i}", BetOdds.STRAIGHT_BET)
            self.wheel.addOutcome(i, outcome)

        straightBetZeroZeroOutcome = Outcome("00", BetOdds.STRAIGHT_BET)
        self.wheel.addOutcome(37, straightBetZeroZeroOutcome)

    def generateSplitBets(self):
        middleCol = [i for i in range(2, 36, 3)]
        for n in middleCol:
            leftSplit = Outcome(f"split {n - 1},{n}", BetOdds.SPLIT_BET)
            self.wheel.addOutcome(n - 1, leftSplit)
            self.wheel.addOutcome(n, leftSplit)

            rightSplit = Outcome(f"split {n},{n + 1}", BetOdds.SPLIT_BET)
            self.wheel.addOutcome(n, rightSplit)
            self.wheel.addOutcome(n + 1, rightSplit)

        for n in range(4, 37):
            upDownSplit = Outcome(f"split {n - 3},{n}", BetOdds.SPLIT_BET)
            self.wheel.addOutcome(n - 3, upDownSplit)
            self.wheel.addOutcome(n, upDownSplit)

    def generateStreetBets(self):
        pass
