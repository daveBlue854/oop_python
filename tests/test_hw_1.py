from unittest import TestCase
from docs import hw

class TestGreeting(TestCase):
    def testExamle(self):
        g= hw.Greeting("x", "y")
        self.assertEqual(str(g), "x y")

    def testShouldGreetNicely(self):
        g = hw.Greeting('x','y')
        res = g.greetNicely()
        self.assertEqual(res,'nice x y')
