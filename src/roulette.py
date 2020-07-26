from dataclasses import dataclass
import random
from enum import IntFlag


class BetOdds(IntFlag):
    STRAIGHT = 35
    SPLIT = 17
    STREET = 11
    CORNER = 8
    FIVE_BET = 6
    LINE = 5
    DOZEN = 2
    COLUMN = 2
    EVEN_MONEY = 1


@dataclass(frozen=True)
class Outcome:
    name: str
    odds: BetOdds

    def winAmount(self, amount: int) -> int:
        return self.odds * amount


class Bin(set):
    pass


class Wheel:
    def __init__(self):
        self.bins = tuple(Bin() for i in range(38))
        self.rng = random.Random()
        self.allOutcomes = dict()

    def getOutcomeByIndex(self, number: int) -> Outcome:
        return self.bins[number]

    def getOutcomeByName(self, name: str) -> Outcome:
        return self.allOutcomes[name]

    def addOutcome(self, number: int, outcome: Outcome) -> None:
        self.allOutcomes[outcome.name] = outcome
        self.bins[number].add(outcome)

    def next(self) -> Outcome:
        randIndex = self.rng.randint(0, 37)
        return self.bins[randIndex]


class BinBuilder:
    def __init__(self, wheel: Wheel):
        self.wheel = wheel

    def buildBins(self) -> None:
        self.straightBets()
        self.splitBets()
        self.streetBets()
        self.cornerBets()
        self.lineBets()
        self.dozenBets()
        self.columnBets()
        self.evenMoneyBets()
        self.fiveBet()

    def straightBets(self) -> None:
        for i in range(37):
            outcome = Outcome(f"{i}", BetOdds.STRAIGHT)
            self.wheel.addOutcome(i, outcome)

        straightBetZeroZeroOutcome = Outcome("00", BetOdds.STRAIGHT)
        self.wheel.addOutcome(37, straightBetZeroZeroOutcome)

    def splitBets(self) -> None:
        middleCol = [i for i in range(2, 36, 3)]
        for n in middleCol:
            leftSplit = Outcome(f"split {n - 1},{n}", BetOdds.SPLIT)
            self.wheel.addOutcome(n - 1, leftSplit)
            self.wheel.addOutcome(n, leftSplit)

            rightSplit = Outcome(f"split {n},{n + 1}", BetOdds.SPLIT)
            self.wheel.addOutcome(n, rightSplit)
            self.wheel.addOutcome(n + 1, rightSplit)

        for n in range(4, 37):
            upDownSplit = Outcome(f"split {n - 3},{n}", BetOdds.SPLIT)
            self.wheel.addOutcome(n - 3, upDownSplit)
            self.wheel.addOutcome(n, upDownSplit)

    def streetBets(self) -> None:
        for i in range(12):
            jump = 3 * i
            relevantNums = (1 + jump, 2 + jump, 3 + jump)
            street = Outcome(f"street {str(relevantNums)}", BetOdds.STREET)
            for num in relevantNums:
                self.wheel.addOutcome(num, street)

    def cornerBets(self) -> None:
        for i in range(1, 32, 3):
            for j in range(2):
                cornerNums = self.__createCornerFromTopLeft(i + j)
                corner = Outcome(f"corner {str(cornerNums)}", BetOdds.CORNER)
                for num in cornerNums:
                    self.wheel.addOutcome(num, corner)

    def __createCornerFromTopLeft(self, i) -> tuple:
        return i, i + 1, i + 3, i + 4

    def lineBets(self) -> None:
        for i in range(1, 32, 3):
            lineNums = tuple(i + j for j in range(6))
            line = Outcome(f"line {str(lineNums)}", BetOdds.LINE)
            for num in lineNums:
                self.wheel.addOutcome(num, line)

    def dozenBets(self) -> None:
        for i in range(3):
            dozenNums = tuple(k + 1 for k in range(i * 12, i * 12 + 12))
            dozen = Outcome(f"dozen {str(dozenNums)}", BetOdds.DOZEN)
            for num in dozenNums:
                self.wheel.addOutcome(num, dozen)

    def columnBets(self) -> None:
        for i in range(3):
            columnNums = tuple(j for j in range(i + 1, 35 + i, 3))
            column = Outcome(f"column {str(columnNums)}", BetOdds.COLUMN)
            for num in columnNums:
                self.wheel.addOutcome(num, column)

    def evenMoneyBets(self) -> None:
        redNums = (1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36)
        red = Outcome(f"red", BetOdds.EVEN_MONEY)
        for num in redNums:
            self.wheel.addOutcome(num, red)

        blackNums = tuple(i for i in range(1, 36) if i not in redNums)
        black = Outcome(f"black", BetOdds.EVEN_MONEY)
        for num in blackNums:
            self.wheel.addOutcome(num, black)

        oddNums = tuple(i for i in range(1, 36) if i % 2 == 1)
        odd = Outcome(f"odd", BetOdds.EVEN_MONEY)
        for num in oddNums:
            self.wheel.addOutcome(num, odd)

        evenNums = tuple(i for i in range(1, 36) if i % 2 == 0)
        even = Outcome(f"even", BetOdds.EVEN_MONEY)
        for num in evenNums:
            self.wheel.addOutcome(num, even)

        lowNums = tuple(i for i in range(1, 36) if i < 19)
        low = Outcome(f"low", BetOdds.EVEN_MONEY)
        for num in lowNums:
            self.wheel.addOutcome(num, low)

        highNums = tuple(i for i in range(1, 36) if i > 19)
        high = Outcome(f"high", BetOdds.EVEN_MONEY)
        for num in highNums:
            self.wheel.addOutcome(num, high)

    def fiveBet(self) -> None:
        fiveBetNums = [0, 37, 1, 2, 3]
        fiveBet = Outcome('fiveBet', BetOdds.FIVE_BET)
        for num in fiveBetNums:
            self.wheel.addOutcome(num, fiveBet)


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
