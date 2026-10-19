import unittest
from greet import greet


class TestGreet(unittest.TestCase):
    def test_greet_world(self):
        self.assertEqual(greet("world"), "Hello, world!")

    def test_greet_empty_string(self):
        self.assertEqual(greet(""), "Hello, world!")

    def test_greet_none(self):
        self.assertEqual(greet(None), "Hello, world!")

    def test_greet_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")


if __name__ == "__main__":
    unittest.main()
