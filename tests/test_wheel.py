import unittest
import random

from src.roulette import Wheel, Outcome, Bin


class testWheel(unittest.TestCase):
    def testInit(self):
        w = Wheel()
        self.assertEqual(len(w.bins), 38)

    def testAddOutcome(self):
        w = Wheel()
        o = Outcome('red', 1)
        w.addOutcome(5, o)
        self.assertEqual(Bin({o}), w.getOutcomeByIndex(5))

    def testNext(self):
        w = Wheel()
        next = w.next()
        self.assertEqual(type(next), type(Bin()))

    def test_randomness(self):
        # arrange
        pseudoRandom = random.Random()
        pseudoRandom.seed(1)
        randomIndices = [pseudoRandom.randint(0, 37) for i in range(10)]
        outcomes = [Outcome(i, 1) for i in range(10)]
        w = Wheel()
        for i in range(10):
            w.addOutcome(randomIndices[i], outcomes[i])

        w.rng.seed(1)
        # act+assert
        for i in range(10):
            self.assertEqual(w.next(), Bin({outcomes[i]}))

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
