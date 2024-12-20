import unittest
from func import say_hello

class TestHello(unittest.TestCase):
    """
    Unit test class for validating the say_hello function.
    """
    
    def test_say_hello(self):
        """
        Test that say_hello() returns the expected string "Hello, World!".
        """
        self.assertEqual(say_hello(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()