from src.BinBuilder import BinBuilder
from src.Game import Game
from src.Player57 import Passenger57
from src.Table import Table
from src.Wheel import Wheel


class Demo():
    def __init__(self):
        pass

    def run(self):
        w = Wheel()
        binBuilder = BinBuilder(w)
        binBuilder.buildBins()
        t = Table([])
        g = Game(t, w)
        p1 = Passenger57(t, w)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)
        g.cycle(p1)


d = Demo()
d.run()
