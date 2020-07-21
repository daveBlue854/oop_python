from unittest import TestCase
from src.roulette import Wheel, BinBuilder, Bin, Outcome, BetOdds


class testBinBuilder(TestCase):
    def init(self):
        w = Wheel()
        a = BinBuilder(w)
        return (a, w)

    def testInit(self):
        w = Wheel()
        binBuilder = BinBuilder(w)
        self.assertEqual(type(binBuilder), type(BinBuilder(w)))
        self.assertEqual(type(binBuilder.wheel.get(0)), type(Bin()))

    def testStraightBets(self):
        (binBuilder, wheel) = self.init()
        binBuilder.straightBets()
        zeroBin = wheel.get(0)
        zeroZeroBin = wheel.get(37)
        oneBin = wheel.get(1)
        self.assertTrue(Outcome("0", BetOdds.STRAIGHT) in zeroBin)
        self.assertTrue(Outcome("00", BetOdds.STRAIGHT) in zeroZeroBin)
        self.assertTrue(Outcome("1", BetOdds.STRAIGHT) in oneBin)

    def testSplitBets(self):
        (binBuilder, wheel) = self.init()
        binBuilder.splitBets()
        oneBin = wheel.get(1)
        thirtySixBin = wheel.get(36)
        self.assertTrue(Outcome("split 1,2", BetOdds.SPLIT) in oneBin)
        self.assertTrue(Outcome("split 1,4", BetOdds.SPLIT) in oneBin)

        self.assertTrue(Outcome("split 35,36", BetOdds.SPLIT) in thirtySixBin)
        self.assertTrue(Outcome("split 33,36", BetOdds.SPLIT) in thirtySixBin)

    def testStreetBets(self):
        (binBuilder, wheel) = self.init()
        binBuilder.streetBets()
        oneBin = wheel.get(1)
        thirtySixBin = wheel.get(36)
        self.assertTrue(Outcome("street (1, 2, 3)", BetOdds.STREET) in oneBin)
        self.assertTrue(Outcome("street (34, 35, 36)", BetOdds.STREET) in thirtySixBin)

    def testCornerBets(self):
        (binBuilder, wheel) = self.init()
        binBuilder.cornerBets()
        oneBin = wheel.get(1)
        twoBin = wheel.get(2)
        fiveBin = wheel.get(5)

        self.assertTrue(Outcome("corner (1, 2, 4, 5)", BetOdds.CORNER) in oneBin)

        self.assertTrue(Outcome("corner (1, 2, 4, 5)", BetOdds.CORNER) in twoBin)
        self.assertTrue(Outcome("corner (2, 3, 5, 6)", BetOdds.CORNER) in twoBin)

        self.assertTrue(Outcome("corner (1, 2, 4, 5)", BetOdds.CORNER) in fiveBin)
        self.assertTrue(Outcome("corner (2, 3, 5, 6)", BetOdds.CORNER) in fiveBin)
        self.assertTrue(Outcome("corner (4, 5, 7, 8)", BetOdds.CORNER) in fiveBin)
        self.assertTrue(Outcome("corner (5, 6, 8, 9)", BetOdds.CORNER) in fiveBin)

    def testLineBets(self):
        (binBuilder, wheel) = self.init()
        binBuilder.lineBets()
        oneBin = wheel.get(1)
        fourBin = wheel.get(4)

        self.assertTrue(Outcome("line (1, 2, 3, 4, 5, 6)", BetOdds.LINE) in oneBin)
        self.assertEqual(len(oneBin), 1)

        self.assertTrue(Outcome("line (1, 2, 3, 4, 5, 6)", BetOdds.LINE) in fourBin)
        self.assertTrue(Outcome("line (4, 5, 6, 7, 8, 9)", BetOdds.LINE) in fourBin)
        self.assertEqual(len(fourBin), 2)
