from io import StringIO
from unittest import TestCase
from unittest.mock import Mock, patch
from docs import hw

class TestGreeting(TestCase):
    def test(self):
        g= hw.Greeting("x", "y")
        self.assertEqual(str(g), "x y")
