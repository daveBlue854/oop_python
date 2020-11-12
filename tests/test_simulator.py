import unittest

from src.BinBuilder import BinBuilder
from src.Game import Game
from src.Player import Player
from src.Player57 import Passenger57
from src.Simulator import Simulator
from src.Table import Table
from src.Wheel import Wheel

"""
what need to be created and tested?
methods and ctor:
session -> List[int]
this method should be called several times  by the second method
every call this method will execute a full session of many cycles, until the player class returns playing()==False
this method will keep calling game.cycle method
"""


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.w = Wheel()
        bb = BinBuilder(self.w)
        bb.buildBins()
        self.t = Table()
        self.p = Passenger57(self.t, self.w)
        self.g = Game(self.t, self.w)
        self.sim = Simulator(self.p, self.g)

    def test_something(self):
        self.assertEqual(type(self.sim), Simulator)

    def testInit(self):
        self.assertTrue(Player in type(self.sim.player).mro())
        self.assertTrue(Game in type(self.sim.game).mro())
        self.assertEqual(self.sim.playerDuration, 250)

    def testDefaultMutableList(self):
        sim1 = Simulator(self.p, self.g)
        sim2 = Simulator(self.p, self.g)
        sim1.maximums.append(1)
        self.assertEqual(len(sim2.maximums), 0)


if __name__ == '__main__':
    unittest.main()
