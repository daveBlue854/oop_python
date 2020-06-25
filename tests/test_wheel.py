import unittest
import random

from src.roulette import Wheel, Outcome, Bin


class testWheel(unittest.TestCase):
    def test_ShouldHaveThirtyEightBins(self):
        w = Wheel()
        self.assertEqual(len(w.bins), 38)

    def test_shouldAddAOutcomeToBinWhenCallingAddOutcome(self):
        w = Wheel()
        o = Outcome('red', 1)
        w.addOutcome(5, o)
        self.assertEqual(Bin({o}), w.get(5))

    def test_sholdGetRandomBinWhenCallingChoose(self):
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


if __name__ == '__main__':
    unittest.main()
