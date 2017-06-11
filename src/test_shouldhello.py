import unittest

from main import hello 

class TestHelloWorld(unittest.TestCase):
    def test_print_hello(self):
        self.assertEqual(hello(), 'Hello World')

if __name__ == '__main__':
    unittest.main()
