import unittest
import random

from src.Bin import Bin
from src.Outcome import Outcome
from src.Wheel import Wheel


class testWheel(unittest.TestCase):
    def testInit(self):
        w = Wheel()
        self.assertEqual(len(w.bins), 38)

    def testAddOutcome(self):
        w = Wheel()
        o = Outcome('red', 1)
        w.addOutcome(5, o)
        self.assertEqual(Bin({o}), w.getBinByIndex(5))

    def testNext(self):
        w = Wheel()
        next = w.next()
        self.assertEqual(type(next), type(Bin()))

    def test_randomness(self):
        # arrange
        pseudoRandom = random.Random()
        pseudoRandom.seed(1)
        randomIndices = [pseudoRandom.randint(0, 37) for _ in range(10)]
        outcomes = [Outcome(i, 1) for i in range(10)]
        zipped = zip(randomIndices, outcomes)
        w = Wheel()
        for z in zipped: w.addOutcome(z[0], z[1])
        w.rng.seed(1)
        # act+assert
        for _ in zipped: self.assertEqual(w.next(), Bin({outcomes[i]}))

    def testGetOutcomeByName(self):
        # arrange
        w = Wheel()
        o = Outcome('red', 1)
        # act
        w.addOutcome(5, o)
        # assert
        self.assertEqual(o, w.getOutcomeByName('red'))


if __name__ == '__main__':
    unittest.main()
