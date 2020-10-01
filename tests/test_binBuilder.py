from unittest import TestCase

from src.BetOdds import BetOdds
from src.Bin import Bin
from src.BinBuilder import BinBuilder
from src.Outcome import Outcome
from src.Wheel import Wheel


class TestBinBuilder(TestCase):
    def __init(self):
        w = Wheel()
        a = BinBuilder(w)
        return a, w

    def testInit(self):
        w = Wheel()
        binBuilder = BinBuilder(w)
        self.assertEqual(type(binBuilder), type(BinBuilder(w)))
        self.assertEqual(type(binBuilder.wheel.getOutcomeByIndex(0)), type(Bin()))

    def testBuildBin(self):
        (binBuilder, wheel) = self.__init()
        binBuilder.buildBins()
        oneBin = wheel.getOutcomeByIndex(1)
        oneBinOutcomes = [Outcome('red', BetOdds.EVEN_MONEY),
                          Outcome('odd', BetOdds.EVEN_MONEY),
                          Outcome('low', BetOdds.EVEN_MONEY),
                          Outcome("1", BetOdds.STRAIGHT),
                          Outcome("split 1,2", BetOdds.SPLIT),
                          Outcome("split 1,4", BetOdds.SPLIT),
                          Outcome("street (1, 2, 3)", BetOdds.STREET),
                          Outcome("corner (1, 2, 4, 5)", BetOdds.CORNER),
                          Outcome("line (1, 2, 3, 4, 5, 6)", BetOdds.LINE),
                          Outcome('dozen (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)', BetOdds.DOZEN),
                          Outcome('column (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34)', BetOdds.COLUMN),
                          Outcome('fiveBet', BetOdds.FIVE_BET)
                          ]
        self.assertCountEqual(oneBinOutcomes, oneBin)

    def testStraightBets(self, ):
        (binBuilder, wheel) = self.__init()
        binBuilder.straightBets()
        zeroBin = wheel.getOutcomeByIndex(0)
        zeroZeroBin = wheel.getOutcomeByIndex(37)
        oneBin = wheel.getOutcomeByIndex(1)
        self.assertIn(Outcome("0", BetOdds.STRAIGHT), zeroBin)
        self.assertIn(Outcome("00", BetOdds.STRAIGHT), zeroZeroBin)
        self.assertIn(Outcome("1", BetOdds.STRAIGHT), oneBin)

    def testSplitBets(self):
        (binBuilder, wheel) = self.__init()
        binBuilder.splitBets()
        oneBin = wheel.getOutcomeByIndex(1)
        thirtySixBin = wheel.getOutcomeByIndex(36)
        self.assertIn(Outcome("split 1,2", BetOdds.SPLIT), oneBin)
        self.assertIn(Outcome("split 1,4", BetOdds.SPLIT), oneBin)

        self.assertIn(Outcome("split 35,36", BetOdds.SPLIT), thirtySixBin)
        self.assertIn(Outcome("split 33,36", BetOdds.SPLIT), thirtySixBin)

    def testStreetBets(self):
        (binBuilder, wheel) = self.__init()
        binBuilder.streetBets()
        oneBin = wheel.getOutcomeByIndex(1)
        thirtySixBin = wheel.getOutcomeByIndex(36)
        self.assertIn(Outcome("street (1, 2, 3)", BetOdds.STREET), oneBin)
        self.assertIn(Outcome("street (34, 35, 36)", BetOdds.STREET), thirtySixBin)

    def testCornerBets(self):
        (binBuilder, wheel) = self.__init()
        binBuilder.cornerBets()
        oneBin = wheel.getOutcomeByIndex(1)
        twoBin = wheel.getOutcomeByIndex(2)
        fiveBin = wheel.getOutcomeByIndex(5)

        self.assertIn(Outcome("corner (1, 2, 4, 5)", BetOdds.CORNER), oneBin)

        self.assertIn(Outcome("corner (1, 2, 4, 5)", BetOdds.CORNER), twoBin)
        self.assertIn(Outcome("corner (2, 3, 5, 6)", BetOdds.CORNER), twoBin)

        self.assertIn(Outcome("corner (1, 2, 4, 5)", BetOdds.CORNER), fiveBin)
        self.assertIn(Outcome("corner (2, 3, 5, 6)", BetOdds.CORNER), fiveBin)
        self.assertIn(Outcome("corner (4, 5, 7, 8)", BetOdds.CORNER), fiveBin)
        self.assertIn(Outcome("corner (5, 6, 8, 9)", BetOdds.CORNER), fiveBin)

    def testLineBets(self):
        (binBuilder, wheel) = self.__init()
        binBuilder.lineBets()
        oneBin = wheel.getOutcomeByIndex(1)
        fourBin = wheel.getOutcomeByIndex(4)

        self.assertIn(Outcome("line (1, 2, 3, 4, 5, 6)", BetOdds.LINE), oneBin)
        self.assertEqual(len(oneBin), 1)

        self.assertIn(Outcome("line (1, 2, 3, 4, 5, 6)", BetOdds.LINE), fourBin)
        self.assertIn(Outcome("line (4, 5, 6, 7, 8, 9)", BetOdds.LINE), fourBin)
        self.assertEqual(len(fourBin), 2)

    def testDozenBets(self):
        (binBuilder, wheel) = self.__init()
        binBuilder.dozenBets()
        oneBin = wheel.getOutcomeByIndex(1)
        thirteenBin = wheel.getOutcomeByIndex(13)
        thirtySixBin = wheel.getOutcomeByIndex(36)

        self.assertIn(Outcome('dozen (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)', BetOdds.DOZEN), oneBin)
        self.assertIn(Outcome('dozen (13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24)', BetOdds.DOZEN), thirteenBin)
        self.assertIn(
            Outcome('dozen (25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)', BetOdds.DOZEN), thirtySixBin)

    def testColumnBets(self):
        (binBuilder, wheel) = self.__init()
        binBuilder.columnBets()
        oneBin = wheel.getOutcomeByIndex(1)
        threeBin = wheel.getOutcomeByIndex(3)
        thirtyFiveBin = wheel.getOutcomeByIndex(35)

        self.assertIn(Outcome('column (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34)', BetOdds.COLUMN), oneBin)
        self.assertIn(
            Outcome('column (2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35)', BetOdds.COLUMN), thirtyFiveBin)
        self.assertIn(Outcome('column (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36)', BetOdds.COLUMN), threeBin)

    def testEvenMoney(self):
        (binBuilder, wheel) = self.__init()
        binBuilder.evenMoneyBets()
        oneBin = wheel.getOutcomeByIndex(1)
        twentyEightBin = wheel.getOutcomeByIndex(28)

        oneBinEvenMoneyOutcomes = [Outcome('red', BetOdds.EVEN_MONEY),
                                   Outcome('odd', BetOdds.EVEN_MONEY),
                                   Outcome('low', BetOdds.EVEN_MONEY)]
        for outcome in oneBinEvenMoneyOutcomes:
            self.assertIn(outcome, oneBin)

        twentyEightBinEvenMoneyOutcomes = [Outcome('black', BetOdds.EVEN_MONEY),
                                           Outcome('even', BetOdds.EVEN_MONEY),
                                           Outcome('high', BetOdds.EVEN_MONEY)]

        for outcome in twentyEightBinEvenMoneyOutcomes:
            self.assertIn(outcome, twentyEightBin)

    def testFiveBet(self):
        (binBuilder, wheel) = self.__init()
        binBuilder.fiveBet()
        fiveBetBins = [wheel.getOutcomeByIndex(0), wheel.getOutcomeByIndex(37), wheel.getOutcomeByIndex(1),
                       wheel.getOutcomeByIndex(2), wheel.getOutcomeByIndex(3)]
        fiveBetOutcome = Outcome('fiveBet', BetOdds.FIVE_BET)
        for fBin in fiveBetBins:
            self.assertIn(fiveBetOutcome, fBin)
