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
        binBuilder.generateStraightBets()
        zeroBin = wheel.get(0)
        zeroZeroBin = wheel.get(37)
        oneBin = wheel.get(1)
        self.assertTrue(Outcome("0", BetOdds.STRAIGHT_BET) in zeroBin)
        self.assertTrue(Outcome("00", BetOdds.STRAIGHT_BET) in zeroZeroBin)
        self.assertTrue(Outcome("1", BetOdds.STRAIGHT_BET) in oneBin)

    def testSplitBets(self):
        (binBuilder, wheel) = self.init()
        binBuilder.generateSplitBets()
        oneBin = wheel.get(1)
        thirtySixBin = wheel.get(36)
        self.assertTrue(Outcome("split 1,2", BetOdds.SPLIT_BET) in oneBin)
        self.assertTrue(Outcome("split 1,4", BetOdds.SPLIT_BET) in oneBin)

        self.assertTrue(Outcome("split 35,36", BetOdds.SPLIT_BET) in thirtySixBin)
        self.assertTrue(Outcome("split 33,36", BetOdds.SPLIT_BET) in thirtySixBin)
