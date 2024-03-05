import unittest

from wordcount.greeter import Greeter

class DojoMarsRover(unittest.TestCase):

    def test_hello_name(self):
        greeter = Greeter()
        self.assertEqual(greeter.greet("Peter"), "Hello Peter")
        # TODO Check that "Hello Peter", greeter.greet("Peter") is equal.
